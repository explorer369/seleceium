'''
Created on 2016-6-23

@author: Administrator
'''
#conding:utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome(executable_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe")
browser.get("http://m12308.f3322.net:8070/login.html")
time.sleep(5)
# assert "登录" in browser.title
elem = browser.find_element_by_name("username") 
elem.send_keys("18975428751" + Keys.RETURN)
time.sleep(1)
elem = browser.find_element_by_name("password") 
elem.send_keys("881218" + Keys.RETURN)
time.sleep(1)
browser.find_element_by_id("startLogin")
time.sleep(1)
browser.find_element_by_xpath("//a[contains(@href,'/schedule/schedulePlan.html')]"[2])
try:
    browser.find_element_by_xpath("//a[contains(@href,'/schedule/schedulePlan.html')]")
except NoSuchElementException:
    assert 0, "can't find seleniumhq"
browser.close()