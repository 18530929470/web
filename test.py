#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time :2020/10/23 19:07
# @Author :wangqinghua
# @File : test.py
# @Software : PyCharm


from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')
driver.implicitly_wait(10)

driver.find_element_by_name("wd").send_keys("周杰伦")
driver.find_element_by_id("su").click()
