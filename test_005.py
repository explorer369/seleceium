# coding=gbk
import os,sys,time,re,xlrd
import log,logging,find
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
global driver,Testtime
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
class AndroidTest(unittest.TestCase):
    func = getattr(__import__('find'),'find_name')
  #  func = getattr(__import__('func'),'find_name')
    def setUp(self):     
        try: 
            #options = webdriver.ChromeOptions()
            #options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
            #self.driver = webdriver.Chrome(chrome_options=options,executable_path="C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe")
            self.driver = webdriver.Firefox()
           # self.driver.get("http://m12308.f3322.net:8070/login.html")
            self.driver.get("http://busi.12308.com/login.html")
        except Exception,e:
            print u'Chrome路径错误'
    def tearDown(self):        
        self.driver.close()
        self.driver.quit()
    def test12308click(self):
        print u"========【case_0001】 12308============="
        self.driver.delete_all_cookies()
        elem = self.driver.find_element_by_name("username") 
        elem.send_keys("18975428751" + Keys.RETURN)
        elem = self.driver.find_element_by_name("password") 
        elem.send_keys("881218" + Keys.RETURN)                 
        #self.func("xpath","//input[@id='startLogin']")
        time.sleep(3)
        self.func('css','li.submenu.open > ul > li > a > span')
        #self.func('xpath','//li[2]/ul/li/a/span')#点击添加线路
        #time.sleep(3)
       # self.assertNotEqual(self.driver.find_element_by_xpath(TEXT),TEXT)
        #添加上车点
       # self.func('id','lbtnadd_s')
       #添加检查点
        #self.assertEqual(self.driver.find_element_by_xpath('//li[2]/ul/li/a/span'),'//li[2]/ul/li/a/span')
        #self.func('link',u'查看班次')
        self.func('link',u'查看班次1')
        
        print u'打印测试效果'
        time.sleep(2)

