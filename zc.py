import scrapy


class ZcSpider(scrapy.Spider):
    name = 'zc'
    allowed_domains = ['zc.cn']
    start_urls = ['http://zc.cn/']

    def parse(self, response):
        pass
