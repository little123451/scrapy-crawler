# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql
from utils.utils import *


class JsonPipeline(object):

    def process_item(self, item, spider):
        line = json.dumps(dict(item))
        self.file.write(line + ",\n")
        return item

    def open_spider(self, spider):
        name = spider.name
        self.file = open(base_dir() + '/data/'+name+'.json', 'w+')
        self.file.write("[\n")

    def close_spider(self, spider):
        self.file.write("]")
        self.file.close()


class MySQLPipeline(object):

    def process_item(self, item, spider):
        print(item.insert())
        # 使用 execute()  方法执行 SQL 查询
        self.cursor.execute("SELECT VERSION()")
        # 使用 fetchone() 方法获取单条数据.
        data = self.cursor.fetchone()
        print("Database version : %s " % data)
        return item

    def open_spider(self, spider):
        # 打开数据库连接
        self.db = pymysql.connect(host="", port='', user="", password="", database="" )
        # 使用 cursor() 方法创建一个游标对象 cursor
        self.cursor = self.db.cursor()

    def close_spider(self, spider):
        # 关闭数据库连接
        self.db.close()