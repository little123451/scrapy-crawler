# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MySQLItem(scrapy.Item):
    """
    对 Item 类进行简单地扩展
    一个 MySQL 扩展样例
    """

    _table = scrapy.Field()

    def __init__(self, *args, **kwargs):
        """
        默认以类名作为入库表名
        可用 table 方法进行修改

        :param args:
        :param kwargs:
        :return:
        """
        super().__init__(*args, **kwargs)
        self.table(type(self).__name__)

    def table(self, table):
        """
        在保存方式为数据库的情况下,设置保存的库

        :param table:
        :return:
        """
        if (table == '') : return self._table
        self._table = table

    def insert(self, _type='REPLACE'):
        """
        构造INSERT语句

        :param _type:
        :return:
        """
        # 判断插入方式
        _map = {
            'INSERT': 'INSERT INTO',
            'IGNORE': 'INSERT IGNORE',
            'REPLACE': 'REPLACE INTO'
        }
        insert_type = _map[_type]

        item = self.items()
        fields = ''
        values = ''
        for key in item:
            fields += '`'+key[0]+'`,'
            if str(key[1]).isdigit() :
                values += str(key[1])+','
            else:
                #todo 过滤插入值中的危险字符,如: \ / < > 等
                values += '`' + str(key[1]) + '`,'
        fields.strip(',')
        values.strip(',')
        return insert_type + ' `' + self._table + '` ' + '('+fields+') VALUES ('+values+');'


class APIItem(scrapy.Item):
    """
    对 Item 类进行简单地扩展
    一个 通过API存储数据的 扩展样例
    """

    _api_key = scrapy.Field()

    def __init__(self, *args, **kwargs):
        """
        默认以类名作为接口 key 索引
        可用 name 方法进行修改

        :param args:
        :param kwargs:
        :return:
        """
        super().__init__(*args, **kwargs)
        self.api_key(type(self).__name__)

    def api_key(self, api_key=''):
        """
        在保存方式为 API 的情况下,设置 API 的索引 Key

        :param api_key:
        :return:
        """
        if (api_key == '') : return self._api_key
        self._api_key = api_key

    def dump(self):
        """
        返回 api_sdk 调用需要的数据,
        :return:
        """
        data = dict(self.items())
        return data
