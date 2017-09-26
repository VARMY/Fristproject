# -*- coding: utf-8 -*-
import scrapy


class XunhuanSpider(scrapy.Spider):
    name = "xunhuan"
    # allowed_domains = ["www.23us.so/list/1_1.html"]

    def start_requests(self):
        for page in range(1,11):
           url = 'http://www.23us.so/list/1_{}.html'.format(str(page))
           yield scrapy.Request(url,callback=self.parse,meta={'page':page})


    def parse(self, response):
        page = response.meta['page']
        print('第%d页'%page)

        for i in response.css('#content tr')[1:]:
            novle_name = i.css('td:nth-of-type(1) a::text').extract()
            print(novle_name)


