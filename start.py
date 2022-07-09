from scrapy import cmdline

def test1():
    cmdline.execute('scrapy crawl novel'.split())

if __name__ == '__main__':
    test1()