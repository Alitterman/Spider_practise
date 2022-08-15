import scrapy


class ZcSpider(scrapy.Spider):
    name = 'zc'
    allowed_domains = ['zc.cn']
    start_urls = ["https://www.itcast.cn/channel/teacher.shtml"]

    def parse(self, response, *args):
        body = response.body.decode('utf-8')
        print(body)
        filename = "teacher.html"
        open(filename, 'a', encoding='UTF-8').write(body)
