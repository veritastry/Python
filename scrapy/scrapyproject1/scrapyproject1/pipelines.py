# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


'''
讲解：
判断当前的Scrapyproject1Pipeline类下面是否有from_crawler方法，如果有的haul，就执行:
                    obj=Scrapyproject1Pipeline.from_crawler(参数)
如果要给构造方法传参，必须要
        obj=Scrapyproject1Pipeline(),（就是ini有from_crawl，返回的也是当前的类对象，传入的参数也可以在init方法里面拿到，就可以在其他方法里面进行调用
如果这个方法的haul，那么这个obj就是当前的类对象
                    obj=from_crawler()


在外部实际的调用
执行顺序：
首先判断当前类下面有没有这个from_crawler方法，
        obj=Scrapyproject1Pipeline.from_crawler(参数),如果有的话，就可以拿到里面的传入的参数，也是执行了init方法
如果没有的haul，就是执行init方法）

在执行open_spider方法,obj.open_spider()
然后执行process_item（在爬虫里面每yield一次就执行一次这个方法，yield item  方法，可能是多次循环执行）obj.process_item()
close_spider方法,obj.close_spider()
'''
class Scrapyproject1Pipeline(object):
    '''开始执行一次'''
    def  __init__(self,path):##这个参数是下面传过来的
        self.f=None
        ##这个的目的一是为了在了一个实例化对象的时候，更好的调用这个方法，而不是通过open来调用这个方法

        self.path=path##可以拿到当前的参数，在后面进行调用
    '''
    第一种：
    obj=Scrapyproject1Pipeline
    obj.f这个是拿不了里面的f的方法，因为没有构造方法__init__
    obj=obj.open_spider()
    obj.f这样才可以拿到里面的f方法
    
    第二种：
    要么是通过__init__方法来直接进行调用里面的f方法 ，obj.f就可以拿到里面的方法了
    '''



##obj=Scrapyproject1Pipeline.from_crawler(参数),判断有没有（注意）
##从这里最开始执行，有的话最开始执行，之后实例化的时候，调用  init方法
    @classmethod
    def   from_crawler(cls,crawler):##这个cls就是当前的类（self）Scrapyproject1Pipeline
        '''
        初始haul的时候，使用的，创建pipeline对象
        :param crawler:
        :return:
        '''
        # val=crawler.settings.getint('')
        path=crawler.settings.get('path')
        ##crawler.settings所有的配置文件，后面是取所有的配置文件里面找这个

        return   cls(path)##返回对象（已经实例化好的对象）cls就是当前类Scrapyproject1Pipeline，在某一个地方已经实例化了这个函数，在这里可以返回这个对象
##下面想当于是传了参数到这个当前的这个类下面，这个里面会返回一个参数到当前类下面




    '''开始执行一次 Scrapyproject1Pipeline.from_crawler(参数).open_spider '''
    def   open_spider(self,spider):
        '''
        爬虫刚开始执行的时候，调用
        :param spider:
        :return:
        '''

        ##如果要为某做特定的爬虫操作的话，可以做判断
        # if  spider.name=='cnblog':
        self.f=open('page_url.log',mode='a+')##在同一个类下面，所以类是相同的,以追加的方式打开
        print('爬虫开始')





    '''
    在这里面会被反复被调用使用，这里面会反复执行
    '''
    def process_item(self, item, spider):
        print('pipeline操作')
        # print(item['text'])
        print('pipelinr',item['url_title'])
        self.f.write('href:'+item['url_title']+'\n')
        print('结束')
        from scrapy.exceptions import DropItem
        raise   DropItem#如果不想让下一个pipeline执行的话，就抛出一个异常
        # return item##作用是返回什么，交给下一个pipeline使用
    '''多个pipeline方法
    这个返回item的作用是为了下一个pipeline使用，如果不返回的话，下一个就不能执行
    执行顺序，都打开open_spider，然后执行下面sprocess_item方法，循环执行，在执行close_spider方法
    '''


    '''最终执行一次'''
    def   close_spider(self,spider):
        self.f.close()
        print('close')

'''
spider就是当前爬虫的（类）对象，item是爬虫yield传过来的已经封装好的对象
可以调用里面的方法
'''




'''
这里是做持久化操作的，可以保存进数据库，也可以保存到文件里面，可以多个pipeline方法，分别保存到不同的地方使用 
'''