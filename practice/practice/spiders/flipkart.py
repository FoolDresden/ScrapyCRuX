import scrapy


class crawlFlip(scrapy.Spider):
    name = 'flip'
    def start_requests(self):
        urls = ['https://www.flipkart.com/search?q=shoes']
        # urls = ['http://quotes.toscrape.com/js/']
        for url in urls:
            yield scrapy.Request(url, callback = self.parse)

    def parse(self, response):
        name = response.css('a._2cLu-l::attr(title)').extract()
        fw = open('writeme.txt', 'w')
        fw.write(str(name))
        link = response.css('div._2kUstJ')
        nxt = link.css('a::attr(href)').extract()
        fw2 = open('nxt.txt', 'w')
        for url in nxt:
            fw2.write(str(link))
            yield response.follow(url, callback = self.parse)
