# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SevenCatsItem(scrapy.Item):
    title = scrapy.Field()
    score = scrapy.Field()
    serialised = scrapy.Field()
    type = scrapy.Field()
    label = scrapy.Field()
    wordcount = scrapy.Field()
    readings = scrapy.Field()
    popularity = scrapy.Field()
    writer = scrapy.Field()
    # writer_lv = scrapy.Field()
    book_num = scrapy.Field()
    writer_word = scrapy.Field()
    days = scrapy.Field()
