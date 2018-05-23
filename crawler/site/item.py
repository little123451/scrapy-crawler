# -*- coding: utf-8 -*-
import scrapy
from items.items import Item

class Spider(scrapy.Spider):
    name = 'Examples'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://finance.sina.com.cn/']

    def parse(self, response):
        item = Item(name = 'title')
        return item
