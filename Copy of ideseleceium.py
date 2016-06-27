'''
Created on 2016-6-23

@author: Administrator
'''
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

browser = webdriver.Chrome(executable_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe")
#browser.get("http://m12308.f3322.net:8070/login.html")
time.sleep(5)
class fff(unittest.TestCase):
    def setUp(self):
        self.driver = browser
        self.driver.implicitly_wait(30)
        self.base_url = "http://m12308.f3322.net:8070/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_12308(self):
        driver = self.driver
        driver.get(self.base_url + "/login.html")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("18975428751")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("18975428751")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("881218")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("881218")
        driver.find_element_by_id("startLogin").click()
        driver.find_element_by_id("startLogin").click()
        driver.find_element_by_xpath("//div[@id='sidebar']/ul/li[2]/ul/li[3]/a/span").click()
        driver.find_element_by_xpath("//div[@id='sidebar']/ul/li[2]/ul/li[3]/a/span").click()
        driver.find_element_by_css_selector("a.select-tit > i").click()
        driver.find_element_by_css_selector("a.select-tit > i").click()
        driver.find_element_by_css_selector("a.select-tit > i").click()
        driver.find_element_by_css_selector("a.select-tit > i").click()
        driver.find_element_by_xpath("//form[@id='searchBox']/div/div/div[6]/div/div/a/i").click()
        driver.find_element_by_xpath("//form[@id='searchBox']/div/div/div[6]/div/div/a/i").click()
        driver.find_element_by_xpath("//form[@id='searchBox']/div/div/div[6]/div/div/div/ul/li[5]").click()
        driver.find_element_by_css_selector("#lbtnSearch > span").click()
        driver.find_element_by_css_selector("#lbtnSearch > span").click()
        driver.find_element_by_css_selector("#lbtnSearch > span").click()
        driver.find_element_by_css_selector("#lbtnSearch > span").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
