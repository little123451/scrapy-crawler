#!/usr/bin/env python
# coding:utf-8

"""
工具函数集合
"""

import time
import os
import re
import random

def base_dir():
    """
    获取项目的根目录

    :return:
    """
    file_path = os.path.split(os.path.realpath(__file__))[0]
    root = file_path + '/../'
    return root


def sub(text):
    # todo 将'多余空格'(2个以上的空格)的定义作为参数传入
    """
    删除给定字符串中的html标签和多余空格

    :param text:
    :return:
    """
    text = re.sub('<.*?>', '', text)
    text = re.sub('\s{2,}', '', text)
    return text.strip()


def real_href(current, href):
    """
    根据页面当前路径和相对路径求出绝对路径

    :param current:     页面当前路径
    :param href:        抓取到的相对路径
    :return:
    """
    if href == '#' or href == '/': return current

    if (current.count('/') > 2):
        base = re.sub('/[^/]*?$', '/', current)
    else:
        base = current + '/'

    if (re.match('^/[^/]', href)):
        base = re.sub('([^/:])/.*', '\g<1>', current)

    if (re.match('^//[^/]', href)):
        return 'http:' + href

    if (re.match('^[^:]+://', href)):
        return href

    url = base + href
    while (re.search('/\./', url)):
        url = re.sub('/\./', '/', url)
    while (re.search('/[^/]*?/\.\./', url)):
        url = re.sub('/[^/]*?/\.\./', '/', url, 1)
    return url.strip('/')


def sleep(seconds=3, rand=False):
    """
    休眠函数

    :param seconds:     休眠秒数
    :param rand:        是否随机休眠
    :return:
    """
    if rand:
        seconds = (random.random() + 1) * seconds
    time.sleep(seconds)
