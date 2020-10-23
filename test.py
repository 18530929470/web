#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time :2020/10/23 19:07
# @Author :wangqinghua
# @File : test.py
# @Software : PyCharm

# coding=utf-8
import unittest
from selenium import webdriver
import time


class forTest(unittest.TestCase):
    # 测试用例初始化
    # 打开谷歌浏览器，并进入百度
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

        self.driver.get('http://www.baidu.com')

    # 测试用例释放
    # 等待 3s，关闭浏览器
    def tearDown(self) -> None:
        time.sleep(3)

        self.driver.quit()

    # 输入‘战狼'，并点击搜索
    def test_1(self):
        pass

        self.driver.find_element_by_id('kw').send_keys('战狼')
        self.driver.find_element_by_id('su').click()

    # 输入‘红海行动'，并点击搜索
    def test_2(self):
        pass

        self.driver.find_element_by_id('kw').send_keys('红海行动')
        self.driver.find_element_by_id('su').click()


if __name__ == '__main__':
    unittest.main()
