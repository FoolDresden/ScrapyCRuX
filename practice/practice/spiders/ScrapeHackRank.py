import scrapy
import scrapy_splash

class Scrape(scrapy.Spider):
    name = 'project'

    def start_requests(self):
        urls = ['https://www.hackerrank.com/login?h_r=community_home&h_v=log_in&h_l=header_right']
        for url in urls:
            yield scrapy.Request(url = url, callback = self.login)


    def login(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata = {'username': 'kumarshreyam0409@gmail.com', 'password': 'pass1234'},
            callback = self.after_login(response)
        )

    def after_login(self, response):
        if 'Invalid login or password. Please try again.' in response.body:
            self.logger.error('login failed!!!')
        else:
            self.logger.error("Login succeeded!")
