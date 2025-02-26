# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient

# class SevenCatsPipeline:
#     def process_item(self, item, spider):
#         return item


class MongoPipeline:
    collection_name = 'seven_cats'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        # 将Scrapy item转换为字典
        item_dict = {
            'title': item['title'], 'score': float(item['score']), 'serialised': item['serialised'],
            'type': item['type'], 'label': item['label'], 'wordcount': float(item['wordcount']),
            'readings': float(item['readings']), 'popularity': float(item['popularity']),
            'writer': item['writer'].strip(), 'book_num': int(item['book_num']),
            'writer_word': float(item['writer_word']), 'days': item['days']    # , 'days': int(item['days'])
        }
        # 插入数据库时会自动生成_id字段
        self.db[self.collection_name].insert_one(item_dict)
        return item

