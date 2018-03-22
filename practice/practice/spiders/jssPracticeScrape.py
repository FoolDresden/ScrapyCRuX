import scrapy
import scrapy_splash

class MySpider(scrapy.Spider):
    name = "jsscraper"

    start_urls = ["http://quotes.toscrape.com/js/"]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy_splash.SplashRequest(url=url, callback=self.parse, endpoint='render.html')

    def parse(self, response):
        fw = open('writeme2.txt', 'w')
        for q in response.css("div.quote"):
            print('executed!!!!!!!!!!!!!!!!!')
            fw.write(str(q) + '\n')
            # fw.write(str(q) + '\n')
