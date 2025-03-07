# scrapy
## 启动爬虫的几种方式

    -命令行工具之scrapy runspider（全局命令）
        1、会读取settings.py
        2、运行数量：单个
    
    -命令行工具之scrapy crawl（项目级命令）
        1、会读取settings.py
        2、运行数量: 单个
    
    -cmdline.execute （单个爬虫用该方式）
        1、会读取settings.py
        2、运行数量：单个（推荐）
    
    -scrapy.crawler.CrawlerProcess （多个爬虫会有干扰）
        1、不读取settings.py（要自己添加配置 from scrapy.utils.project import get_project_settings）
        2、运行数量: 单个、多个
    
    -scrapy.crawler.CrawlerRunner （多个爬虫用该方式）
        1、不读取settings.py（要自己添加配置 from scrapy.utils.project import get_project_settings）
        2、运行数量: 单个、多个（推荐）

## 爬虫暂停

    scrapy crawl xxxspider -s JOBDIR=crawls/xxxspider-1

## spider

### __init__

### start_requests

### parse

## 下载中间件的方法

    process_request(request，spider): 所有请求都会调用此方法，增加了selenium解析页面，请求太多一直重复打开关闭。
    process_response(request, response, spider)： 这里的参数比上面的多了response，肯定是用来处理response的
    process_exception(request, exception, spider)：处理异常
    from_crawler(cls, crawler)：从settings.py获取配置
    
    ##　下载中间件：
    -- 下载中间件用于操作向互联网发起请求的request和返回的response，比如修改请求头、修改响应、管理cookies、丢弃非200状态码响应、丢弃非指定域名请求等；

## 蜘蛛中间件的方法

    process_spider_input(response, spider)：所有请求都会调用这个方法
    process_spider_output(response, result, spider)：spider解析完response之后调用该方法，result就是解析的结果(是一个可迭代对象)，其中可能是items也可能是request对象
    process_spider_exception(response, exception, spider)：处理异常
    process_start_requests(start_requests, spider)：同process_spider_output，不过只处理spider中start_requests方法返回的结果
    from_crawler(cls, crawler)：从settings.py获取配置
    
    ## spider 中间件：
    -- 一般用于操作 spider 返回的request，比如记录深度、丢弃非200状态码响应、丢弃非指定域名请求等；
    -- 蜘蛛中间件一般不需要自己编写，使用内置的几个也足够了；

## 自定义spider和pipeline

## xpath语法
1. 查找下一页 `//div[@class='page']/a[text()='下一页']`
2. 获取标签内容 `el_song.xpath("./a/text()").get()`
3. 获取标签href属性 `netx_el.xpath("./@href").get()`



## 数据保存

# 反爬
## 自动延迟
## user-agent伪装
## ip代理池
## 降低频率（模拟自然人）
## 验证码
