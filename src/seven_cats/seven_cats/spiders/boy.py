import scrapy
from src.seven_cats.seven_cats.items import SevenCatsItem


class BoySpider(scrapy.Spider):
    name = "boy"
    allowed_domains = ["www.qimao.com"]
    # 前453页为平台原创小说，后面全部没有签约和作家天数的信息，因此代码有所改变。
    # 另外其中有很多没有评分小说未爬取，它们本身为异常值，如只写两章就被平台签约但没人评论的异常数据。
    # 预计爬取9990条数据，最终爬取7718条数据。
    start_urls = [f"https://www.qimao.com/shuku/0-a-a-a-a-a-a-click-{k}/" for k in range(452, 667)]
    # start_urls = ["https://www.qimao.com/shuku/0-a-a-a-a-a-a-click-1/"]

    def parse(self, response):
        # 获取详情页链接
        hrefs = response.xpath('.//div[@class="pic"]/a/@href').getall()
        for href in hrefs:
            # 发起详情页请求，并指定回调函数
            yield scrapy.Request('https://www.qimao.com/' + href, callback=self.parse_detail)

    def parse_detail(self, response):
        # 解析详情页数据
        item = SevenCatsItem()
        item['title'] = response.xpath('//*[@class="wrap-txt"]/div[1]/span[1]/text()').get()
        item['score'] = response.xpath('//*[@class="wrap-txt"]/div[1]/span[2]/text()').get()
        item['serialised'] = response.xpath('//*[@class="wrap-txt"]/div[2]/em[1]/text()').get()
        # item['type'] = response.xpath('//*[@class="wrap-txt"]/div[2]/em[3]/a/text()').get()
        item['type'] = response.xpath('//*[@class="wrap-txt"]/div[2]/em[2]/a/text()').get()
        # item['label'] = response.xpath('//*[@class="wrap-txt"]/div[2]/em[4]/a/text()').get()
        item['label'] = response.xpath('//*[@class="wrap-txt"]/div[2]/em[3]/a/text()').get()
        item['wordcount'] = response.xpath('//*[@class="wrap-txt"]/div[4]/span[1]/em/text()').get()
        item['readings'] = response.xpath('//*[@class="wrap-txt"]/div[4]/span[2]/em/text()').get()
        item['popularity'] = response.xpath('//*[@class="wrap-txt"]/div[4]/span[3]/em/text()').get()
        item['writer'] = response.xpath('//*[@class="author-information right"]/div/div[2]/div/a/text()').get()
        item['book_num'] = response.xpath('//*[@class="author-information right"]/ul/li[1]/div[1]/em/text()').get()
        item['writer_word'] = response.xpath('//*[@class="author-information right"]/ul/li[2]/div[1]/em/text()').get()
        # item['days'] = response.xpath('//*[@class="author-information right"]/ul/li[3]/div[1]/em/text()').get()
        item['days'] = None

        # 返回包含数据的item对象
        yield item
