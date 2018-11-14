from   scrapy.dupefilter import  BaseDupeFilter
from   scrapy.utils.request import   request_fingerprint##进行加密，url的唯一标识，会进行加密处理
'''
在scrapy里面有一个唯一标识
http://xxx.com/?k1=v1&k2=v2
http://xxx.com/?k2=v2&k1=v1
如果是md5进行加密的话，这两个url是不一样的，但是这两个url是相同的
但是scrapy里面有一个方法，可以辨别出两个相同的url出来
request_fingerprint(放在里面进行加密，如果是相同的打印出来也是相同的)
'''


##去重

class  Self_Dupliter(BaseDupeFilter):
    def  __init__(self):
        self.vister_urls=set()
        ##设置url元祖


    @classmethod
    def from_settings(cls, settings):
        print('最开始')
        return cls()

    # def request_seen(self, request):###传入的requets里面有url，可以直接取出来
    #     print('执行去重规则')
    #     if   request.url  in  self.vister_urls:
    #         return   True
    #     self.vister_urls.add(request.url)
        # return False

    def request_seen(self, request):  ###传入的requets里面有url，可以直接取出来
        print('执行去重规则')
        print(request.url)
        fd=request_fingerprint(request)##进行了加密处理，长度一样
        if fd in self.vister_urls:##如果访问的url在这里的话，就返回true，不执行
            print('存在')
            print(request.url)
            return True
        self.vister_urls.add(fd)


##爬虫开始的时候
    def open(self):  # can return deferred
        print('开始')

##redis，爬虫结束
    def close(self, reason):  # can return a deferred
        print('结束')


##记录日志的时候
    def log(self, request, spider):  # log that a request has been filtered
        print('记录日志')


'''
可以让他每次来不执行init方法
直接是下面的方法,所以init里面定义的元祖可以一直加值，在判断

执行顺序：
最开始执行settings（有执行去重类，导入模块的时候）
在执行parse方法，如果settings里面配置了去重的类的话，那么每yield Requets的时候，就会执行这个自定义的去重类：
去重类》》先执行from_seen，在执行open，在执行request_seen（多次执行，每yield Request一次的haul，就执行一次这个方法），最后执行close
'''