
from scrapy import cmdline
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from twisted.internet import reactor
from novel_scrapy.spiders.novel_spider import NovelSpider

def test1():
    cmdline.execute('scrapy crawl novel'.split())

if __name__ == '__main__':

    configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
    runner = CrawlerRunner()
    runner.crawl(NovelSpider)
    d = runner.join() # 返回一个Twisted中的Deferred对象
    d.addBoth(lambda _:reactor.stop())
    reactor.run()