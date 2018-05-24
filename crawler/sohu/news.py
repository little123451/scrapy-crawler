# -*- coding: utf-8 -*-
import scrapy
from config.items import News
from utils.utils import *

class Spider(scrapy.Spider):
    name = 'Examples'
    allowed_domains = ['sohu.com']
    start_urls = [
        # 'http://www.sohu.com',
        'http://www.sohu.com/a/232598865_115479'
    ]

    def parse(self, response):

        # 链接发现
        links = response.selector.xpath('//a/@href').re('.*?/a/.+')
        for link in links:
            link = real_href(response.url, link)
            yield scrapy.Request(url=link, callback=self.parse)

        # 数据采集
        title = response.selector.xpath('//h1/text()').extract()[0]
        datetime = response.selector.re('meta property="og:release_date" content="(.*?)"')[0]
        origin = response.selector.re('<span data-role="original-link">来源:(.*?)</span>')[0]
        url = response.url
        item = News(title=title, url=url, datetime=datetime, origin=sub(origin))
        yield item