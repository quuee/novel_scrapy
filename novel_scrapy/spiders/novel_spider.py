
import scrapy

from novel_scrapy.items import NovelScrapyItem


class NovelSpider(scrapy.Spider):
    name = "novel"
    start_urls = ["https://www.mayiwxw.com/79_79726"]

    def parse(self, response):
        el_list = response.xpath("//div[@id='list']/dl/dd/a")
        for el in el_list:
            title = el.xpath("./text()").get()
            href = el.xpath("./@href").get()
            print(f"章节：{title}，链接：{href}")
            if href is not None:
                yield response.follow(href, callback=self.parse_chapter)


    def parse_chapter(self, response):
        title = response.xpath("//div[@class='bookname']/h1/text()").get()
        txt = response.xpath("//div[@id='content']/text()").getall()
        novel = NovelScrapyItem()

        url = response.request.url
        url = url[url.rindex("/")+1:url.rindex(".")]
        novel["sort"] = int(url)
        novel["title"] = title
        novel["content"] = "\n".join(txt)
        yield novel
