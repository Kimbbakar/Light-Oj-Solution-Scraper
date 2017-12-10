# -*- coding: utf-8 -*-
import scrapy


class LojSpider(scrapy.Spider):
    name = 'loj'
    allowed_domains = ['lightoj.com']
    start_urls = ['http://lightoj.com/']

    def parse(self, response):
        pass
