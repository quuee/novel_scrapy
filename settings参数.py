# 项目名称
BOT_NAME = '$project_name'

SPIDER_MODULES = ['$project_name.spiders']
NEWSPIDER_MODULE = '$project_name.spiders'

# 在项目处理器（也称为“ 项目管道”）中并行处理的最大并发项目数（每个响应），默认100。
#CONCURRENT_ITEMS = 100

# Scrapy下载器将执行的并发（即，并发）请求的最大数量，默认16
CONCURRENT_REQUESTS = 8

# 从同一网站下载连续页面之前，下载程序应等待的时间（以秒为单位）。
# 这可以用来限制爬网速度，以避免对服务器造成太大的冲击。支持小数。
# 默认情况下，Scrapy不会在请求之间等待固定的时间，而是使用0.5 * DOWNLOAD_DELAY和1.5 * DOWNLOAD_DELAY之间的随机间隔。
#DOWNLOAD_DELAY = 0

# 将对任何单个域执行的并发（即，并发）请求的最大数量，默认8
#CONCURRENT_REQUESTS_PER_DOMAIN = 16

# 将对任何单个IP执行的并发（即，并发）请求的最大数量，默认0。
# 如果非0，CONCURRENT_REQUESTS_PER_DOMAIN这个参数会被忽略，即按IP不按域名。DOWNLOAD_DELAY也是按IP
#CONCURRENT_REQUESTS_PER_IP = 16

# 将用于实例化Scrapy shell中的项目的默认类
#DEFAULT_ITEM_CLASS = 'scrapy.item.Item'

# 对于任何站点，将允许爬网的最大深度。如果为零，则不施加限制
#DEPTH_LIMIT = 0

# 根据DEPTH_PRIORITY的值取决于深度优先或广度优先，即正值为广度优先(BFO)，负值为深度优先(DFO)
# 计算公式：request.priority = request.priority - ( depth * DEPTH_PRIORITY )
#DEPTH_PRIORITY = 0

# 是否启用cookie
COOKIES_ENABLED = False

# 如果启用，Scrapy将记录请求中发送的所有cookie（即Cookie 标头）和响应中接收的所有cookie（即Set-Cookie标头）
#COOKIES_DEBUG = False

# 是否收集详细的深度统计信息。如果启用此功能，则在统计信息中收集每个深度的请求数
#DEPTH_STATS_VERBOSE = False

# 是否启用DNS内存缓存
#DNSCACHE_ENABLED = True

# DNS内存缓存大小
#DNSCACHE_SIZE = 10000

# 处理DNS查询的超时时间（以秒为单位）。支持浮动
#DNS_TIMEOUT = 60

# 用于爬网的下载器
#DOWNLOADER = 'scrapy.core.downloader.Downloader'

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# 包含您的项目中启用的下载器中间件及其命令的字典
#DOWNLOADER_MIDDLEWARE = {}

# 用于Scrapy HTTP请求的默认标头。它们被填充在 DefaultHeadersMiddleware
DEFAULT_REQUEST_HEADERS = {
}

# Scrapy中默认启用的下载程序中间件的字典。低值更接近引擎，高值更接近下载器，
# 不要试图修改此设置，请修改DOWNLOADER_MIDDLEWARE
#DOWNLOADER_MIDDLEWARES_BASE = {
#     'scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware': 100,
#     'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware': 300,
#     'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware': 350,
#     'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware': 400,
#     'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': 500,
#     'scrapy.downloadermiddlewares.retry.RetryMiddleware': 550,
#     'scrapy.downloadermiddlewares.ajaxcrawl.AjaxCrawlMiddleware': 560,
#     'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware': 580,
#     'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 590,
#     'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': 600,
#     'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': 700,
#     'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 750,
#     'scrapy.downloadermiddlewares.stats.DownloaderStats': 850,
#     'scrapy.downloadermiddlewares.httpcache.HttpCacheMiddleware': 900,
# }

# 是否启用下载器统计信息收集
#DOWNLOADER_STATS = True

# 包含在项目中启用的请求下载处理程序的字典
#DOWNLOAD_HANDLERS = {}

# 包含请求下载处理程序的默认字典
# 如果要禁用FTP处理程序，请设置DOWNLOAD_HANDLERS = {'ftp': None}
#DOWNLOAD_HANDLERS_BASE = {
#     'file': 'scrapy.core.downloader.handlers.file.FileDownloadHandler',
#     'http': 'scrapy.core.downloader.handlers.http.HTTPDownloadHandler',
#     'https': 'scrapy.core.downloader.handlers.http.HTTPDownloadHandler',
#     's3': 'scrapy.core.downloader.handlers.s3.S3DownloadHandler',
#     'ftp': 'scrapy.core.downloader.handlers.ftp.FTPDownloadHandler',
# }

# 下载程序的超时时间（以秒为单位）
#DOWNLOAD_TIMEOUT = 180

# 载程序将下载的最大响应大小（以字节为单位,默认1024MB），为0则不限制
#DOWNLOAD_MAXSIZE = 1073741824

# 下载程序将开始警告的响应大小（以字节为单位，默认32MB）
#DOWNLOAD_WARNSIZE = 33554432

# 声明的Content-Length与服务器发送的内容不匹配，是否触发异常ResponseFailed([_DataLoss]) 
# 如果为False，可以在爬虫文件中判断并处理 if 'dataloss' in response.flags: 
#DOWNLOAD_FAIL_ON_DATALOSS = True

# 用于检测和过滤重复请求的类
#DUPEFILTER_CLASS = 'scrapy.dupefilters.RFPDupeFilter'

# 默认情况下，RFPDupeFilter仅记录第一个重复的请求。设置DUPEFILTER_DEBUG为True它将记录所有重复的请求。
#DUPEFILTER_DEBUG = False

# 包含您的项目中启用的扩展及其顺序的字典
#EXTENSIONS = {}

# 包含默认情况下在Scrapy中可用的扩展程序及其顺序的字典
#EXTENSIONS_BASE = {
#     'scrapy.extensions.corestats.CoreStats': 0,
#     'scrapy.extensions.telnet.TelnetConsole': 0,
#     'scrapy.extensions.memusage.MemoryUsage': 0,
#     'scrapy.extensions.memdebug.MemoryDebugger': 0,
#     'scrapy.extensions.closespider.CloseSpider': 0,
#     'scrapy.extensions.feedexport.FeedExporter': 0,
#     'scrapy.extensions.logstats.LogStats': 0,
#     'scrapy.extensions.spiderstate.SpiderState': 0,
#     'scrapy.extensions.throttle.AutoThrottle': 0,
# }

# 包含要使用的项目管道及其顺序的字典。值是任意的，但是习惯上将它们定义在0-1000范围内。低值优先于高值
#ITEM_PIPELINES = {}

# 是否启用日志记录
#LOG_ENABLED = True

# 用于日志记录的编码
#LOG_ENCODING = 'utf-8'

# 用于记录输出的文件名
#LOG_FILE = None

# 用于格式化日志消息的字符串
#LOG_FORMAT = '%(asctime)s [%(name)s] %(levelname)s: %(message)s'

# 用于格式化日期/时间的字符串，用于改变LOG_FORMAT 中的asctime占位符
#LOG_DATEFORMAT = '%Y-%m-%d %H:%M:%S'

# 用于格式化不同操作的日志消息的类
#LOG_FORMATTER = "scrapy.logformatter.LogFormatter"

# 最低记录级别, 可用：CRITICAL, ERROR, WARNING, INFO, DEBUG
#LOG_LEVEL = 'DEBUG'

# 如果为True，所有标准输出（和错误）将被重定向到日志，例如print也会被记录在日志
#LOG_STDOUT = False

# 如果为True，则日志将仅包含根路径;如果设置为False，则显示负责日志输出的组件
#LOG_SHORT_NAMES = False

# 每次统计记录打印输出之间的间隔（以秒为单位）
#LOGSTATS_INTERVAL = 60.0

# 是否启用内存调试
#MEMDEBUG_ENABLED = False

# 启用内存调试后，如果此设置不为空，则会将内存报告发送到指定的邮箱地址，否则该报告将被写入日志。
# 例如：MEMDEBUG_NOTIFY = ['user@example.com']
#MEMDEBUG_NOTIFY = []

# 是否启用内存使用扩展。此扩展跟踪该进程使用的峰值内存（将其写入统计信息）。
# 当超过内存限制时，它还可以选择关闭Scrapy进程，并在发生这种情况时通过电子邮件通知
#MEMUSAGE_ENABLED = True

# 关闭Scrapy之前允许的最大内存量
#MEMUSAGE_LIMIT_MB = 0

#MEMUSAGE_CHECK_INTERVAL_SECONDS = 60.0

# 电子邮件列表，用于通知是否已达到内存限制
#MEMUSAGE_NOTIFY_MAIL = False

# 发送警告电子邮件通知最大内存之前允许的最大内存量（以兆字节为单位）。如果为零，则不会发出警告
#MEMUSAGE_WARNING_MB = 0

# 使用genspider命令创建爬虫的模板
#NEWSPIDER_MODULE = ""

# 如果启用，Scrapy将在从同一网站获取请求的同时等待随机的时间（介于0.5 * DOWNLOAD_DELAY和1.5 *之间DOWNLOAD_DELAY）
#RANDOMIZE_DOWNLOAD_DELAY = True

# Twisted Reactor线程池大小的最大限制。这是各种Scrapy组件使用的通用多用途线程池。
# 线程DNS解析器，BlockingFeedStorage，S3FilesStore仅举几例。
# 如果遇到阻塞IO不足的问题，请增加此值。
#REACTOR_THREADPOOL_MAXSIZE = 10

# 定义可以重定向请求的最长时间。超过此最大值后，将按原样返回请求的响应
#REDIRECT_MAX_TIMES = 20

# 调整重定向请求的优先级，为正则优先级高
#REDIRECT_PRIORITY_ADJUST = 2

# 调整重试请求的优先级
#RETRY_PRIORITY_ADJUST = -1

# 是否遵循robot协议
ROBOTSTXT_OBEY = False

# 用于解析robots.txt文件的解析器后端
#ROBOTSTXT_PARSER = 'scrapy.robotstxt.ProtegoRobotParser'

#ROBOTSTXT_USER_AGENT = None

# 用于爬网的调度程序
#SCHEDULER = 'scrapy.core.scheduler.Scheduler'

# 设置为True将记录有关请求调度程序的调试信息
#SCHEDULER_DEBUG = False

# 调度程序将使用的磁盘队列的类型。其他可用类型：scrapy.squeues.PickleFifoDiskQueue，
# scrapy.squeues.MarshalFifoDiskQueue， scrapy.squeues.MarshalLifoDiskQueue
#SCHEDULER_DISK_QUEUE = 'scrapy.squeues.PickleLifoDiskQueue'

# 调度程序使用的内存队列的类型。其他可用类型： scrapy.squeues.FifoMemoryQueue
#SCHEDULER_MEMORY_QUEUE = 'scrapy.squeues.LifoMemoryQueue'

# 调度程序使用的优先级队列的类型。另一种可用的类型是 scrapy.pqueues.DownloaderAwarePriorityQueue
#SCHEDULER_PRIORITY_QUEUE = 'scrapy.pqueues.ScrapyPriorityQueue'

# 正在处理响应数据的软限制（以字节为单位）。
# 如果所有正在处理的响应的大小总和高于此值，Scrapy不会处理新的请求
#SCRAPER_SLOT_MAX_ACTIVE_SIZE  = 5_000_000

# 包含您的项目中启用的蜘蛛合约的字典，用于测试蜘蛛
#SPIDER_CONTRACTS = {}

# 包含Scrapy合同中默认启用的Scrapy合同的字典
#SPIDER_CONTRACTS_BASE  = {
#     'scrapy.contracts.default.UrlContract' : 1,
#     'scrapy.contracts.default.ReturnsContract': 2,
#     'scrapy.contracts.default.ScrapesContract': 3,
# }

# 将用于加载蜘蛛的类
#SPIDER_LOADER_CLASS = 'scrapy.spiderloader.SpiderLoader'

# 包含您的项目中启用的蜘蛛中间件及其命令的字典
#SPIDER_MIDDLEWARES = {}

#SPIDER_MIDDLEWARES_BASE = {
#     'scrapy.spidermiddlewares.httperror.HttpErrorMiddleware': 50,
#     'scrapy.spidermiddlewares.offsite.OffsiteMiddleware': 500,
#     'scrapy.spidermiddlewares.referer.RefererMiddleware': 700,
#     'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware': 800,
#     'scrapy.spidermiddlewares.depth.DepthMiddleware': 900,
# }

# Scrapy将在其中寻找蜘蛛的模板列表
#SPIDER_MODULES  = {}

# 用于收集统计信息的类
#STATS_CLASS = 'scrapy.statscollectors.MemoryStatsCollector'

# 蜘蛛完成后，将Scrapy统计信息转储到Scrapy日志中
#STATS_DUMP = True

# 蜘蛛抓取完毕后发送Scrapy统计信息的邮箱列表
#STATSMAILER_RCPTS = []

# 指定是否 将启用telnet控制台
#TELNETCONSOLE_ENABLED = True

# 用于telnet控制台的端口范围。如果设置为None或0，则使用动态分配的端口
#TELNETCONSOLE_PORT = [6023, 6073]

# 使用startproject命令创建新项目和使用 genspider命令创建新的Spider时要在其中查找模板的目录
#TEMPLATES_DIR = "templates"

# 允许抓取的URL的最大URL长度
#URLLENGTH_LIMIT = 2083

# 爬网时使用的默认User-Agent
#USER_AGENT = "Scrapy/VERSION (+https://scrapy.org)"
