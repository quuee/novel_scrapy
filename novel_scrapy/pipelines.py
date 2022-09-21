# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
# from itemadapter import ItemAdapter

# from novel_scrapy.items import NovelScrapyItem
import pandas as pd


class NovelScrapyPipeline:

    def __init__(self):
        self.book = pd.DataFrame(
            columns=["sort", "title", "content"], index=[0])

    def process_item(self, item, spider):
        item_dict = {
            "sort": item["sort"], "title": item["title"], "content": item["content"]}
        book_new = pd.DataFrame(item_dict, index=[0])
        self.book = pd.concat([self.book, book_new], axis=0, ignore_index=True)
        

    def close_spider(self, spider):
        store_file = "/home/cx/Documents/temp.txt"
        if not os.path.exists(store_file):
            os.mknod(store_file)
        self.file = open(store_file, "a", encoding="utf-8")
        # 网上看到用pandas排序
        self.book = self.book.sort_values("sort", ascending=True)

        title_list = list(self.book["title"])
        content_list = list(self.book["content"])
        for i in range(len(title_list)):
            # print(type(title_list[i]))
            # print(title_list[i])
            self.file.write(str(title_list[i])+"\n")
            # \r对应的ASCII码为：0xd，\n对应的ASCII码为：0xa
            self.file.write(str(content_list[i]).replace(
                "\xa0", "").replace("\r", "\n")+"\n")

        self.file.close()

