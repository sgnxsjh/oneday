#!/usr/bin/env python
#-*-coding:utf-8-*-
#coder:sjh
#version:1.0

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class BaiDuChrome(unittest.TestCase):
    def setUp(self):
        self.executable_path = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
        #self.option = webdriver.ChromeOptions()
        #self.option.add_argument("test-type")
        #self.driver = webdriver.Chrome(executable_path=self.executable_path, chrome_options = self.option)
        self.driver = webdriver.Chrome(executable_path=self.executable_path)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    # def tearDown(self):
    #     self.driver.quit()
    #     self.assertEqual([],self.verificationErrors)

    def test_open_and_search(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        time.sleep(3)
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("selenium ide")
        time.sleep(3)
        driver.find_element_by_name("wd").send_keys(Keys.SPACE)
        time.sleep(3)
        driver.find_element_by_name("wd").send_keys(u"教程")
        # driver.find_element_by_name("wd").send_keys("xy") 英文例子
        # 中文例子，中文字符串前面必须加u，表示Unicode字符串
        driver.find_element_by_name("wd").send_keys(Keys.BACK_SPACE * 2)
        driver.find_element_by_id("su").click()

    # def test_XXX(self):
    #     self.assertTrue(True)
    #     print"hello"


if __name__ == "__main__":
    unittest.main()