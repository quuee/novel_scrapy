
import scrapy

from novel_scrapy.items import NovelScrapyItem


class NovelSpider(scrapy.Spider):
    name = "novel"
    start_urls = ["https://www.31xiaoshuo.com/183/183416/"]

    def parse(self, response):
        # print(type(response))
        el_list = response.xpath("//div[@id='list']/dl/dd/a")
        # print(type(el_list))
        for el in el_list:
            # print(el)
            title = el.xpath("./text()").extract()
            # print(type(title))
            href = el.xpath("./@href").extract()
            # print(type(href))
            print(title[0]+" -- "+href[0])
            if href is not None:
                yield response.follow(href[0], callback=self.parse_chapter)


    def parse_chapter(self, response):
        title = response.xpath("//div[@class='bookname']/h1/text()").get()
        txt = response.xpath("//div[@id='content']/text()").extract()
        novel = NovelScrapyItem()

        # https://www.81zw.com/book/45501/20758145.html
        url = response.request.url
        url = url[url.rindex("/")+1:url.rindex(".")]
        novel["sort"] = int(url)
        novel["title"] = title
        novel["content"] = "\n".join(txt)
        yield novel
