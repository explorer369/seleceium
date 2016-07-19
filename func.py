#_*_coding:gb2312
import os,sys,time,re,subprocess
import log,logging
import unittest
from selenium.common.exceptions import NoSuchElementException
from  selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
reload(sys)
sys.setdefaultencoding('GBK')


global driver,Testtime
localpath = os.getcwd()
#logger = log.Logger('rst/log.log',clevel = logging.DEBUG,Flevel = logging.INFO)
def cleanEnv():
    '''每次执行命令时就把此rst目录删除,然后再新建rst,相当于清空上次的测试结果和日志
    '''                        
    os.system('adb kill-server')
    needClean = ['log.log','img','rst']   # 定义这=log.log,img,rst这三个值
    pwd = os.getcwd()                     # pwd=当前文件目录
    for i in needClean:                   # 循环needClean
        delpath = os.path.join(pwd,i)     # 结果为：当前目录\img和当前目录\rst  （例：C:\Users\Administrator\Desktop\测试结果\img）
        if os.path.isfile(delpath):
            cmd = 'del /f/s/q "%s"'% delpath   # 删除delpath得到的两个文件夹（img和rst）/F 强制删除只读文件/S 从所有子目录删除指定文件/Q 安静模式。删除全局通配符时，不要求确认。
            os.system(cmd)
        elif os.path.isdir(delpath):       # 否则，删除delpath得到的两个文件夹（img和rst）
            cmd = 'rd /s/q "%s"' %delpath
            os.system(cmd)
    if not os.path.isdir('rst/screenshot'):
     #   os.makedirs('rst')          
        os.makedirs('rst/screenshot/Failed')
        os.makedirs('rst/screenshot/Passed')
cleanEnv() #让导入此文件时就执行清除件和新建文件
logger = log.Logger('rst/log.log',clevel = logging.DEBUG,Flevel = logging.INFO)
        
def find_name(self,method,TEXT,number=0):
#    self.driver = webdriver.Chrome(executable_path="C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe")
#    self.driver.get("http://m12308.f3322.net:8070/login.html")        
    Testtime=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    if method == "name":
        try:
            emmm = self.driver.find_element_by_name(TEXT)
            #self.assertIsNotNone(emm)
            logger.info('+PASS+  Find the"%s"element'%TEXT)
            emmm.click()
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  Click on the "%s" element to succeed??Already screenshot'%TEXT)
        except NoSuchElementException, e:
          # print logger.info("Did not get to the control, click failed")
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.info('+FAIL+  not found"%s"element ??Already screenshot'%TEXT)
          # return True   #??????????????????????????????????????????????????????
    if method == "class_name":
        try:
            emmm = self.driver.find_element_by_class_name(TEXT)
            #self.assertIsNotNone(emm)
            logger.info('+PASS+  Find the"%s"element'%TEXT)
            emmm.click()
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  Click on the "%s" element to succeed??Already screenshot'%TEXT)
        except NoSuchElementException, e:
          # print logger.info("Did not get to the control, click failed")
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.info('+FAIL+  not found"%s"element ??Already screenshot'%TEXT)
          # return True   #??????????????????????????????????????????????????????
    if method == "css_selector":
        try:
            emmm = self.driver.find_element_by_css_selector(TEXT)
            #self.assertIsNotNone(emm)
            logger.info('+PASS+  Find the"%s"element'%TEXT)
            emmm.click()
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  Click on the "%s" element to succeed??Already screenshot'%TEXT)
        except NoSuchElementException, e:
          # print logger.info("Did not get to the control, click failed")
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.info('+FAIL+  not found"%s"element ??Already screenshot'%TEXT)
          # return True   #??????????????????????????????????????????????????????
    
    if method == "id":
        try:
            emmm = self.driver.find_element_by_id(TEXT)
            #self.assertIsNotNone(emm)
            logger.info('+PASS+  Find the"%s"element'%TEXT)
            emmm.click()
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  Click on the "%s" element to succeed??Already screenshot'%TEXT)
        except NoSuchElementException, e:
            time.sleep(1)
          # print logger.info("Did not get to the control, click failed")
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print e
            print logger.info('+FAIL+  not found"%s"element ??Already screenshot'%TEXT)
          # return True
    if method == "link_text":
        try:
            emmm = self.driver.find_element_by_link_text(TEXT)
            #self.assertIsNotNone(emm)
            logger.info('+PASS+  Find the"%s"element'%TEXT)
            emmm.click()
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  Click on the "%s" element to succeed??Already screenshot'%TEXT)
        except NoSuchElementException, e:
            time.sleep(1)
          # print logger.info("Did not get to the control, click failed")
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.info('+FAIL+  not found"%s"element ??Already screenshot'%TEXT)
          # return True
    if method == "partial_link_text":
        try:
            emmm = self.driver.find_element_by_partial_link_text(TEXT)
            #self.assertIsNotNone(emm)
            logger.info('+PASS+  Find the"%s"element'%TEXT)
            emmm.click()
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  Click on the "%s" element to succeed??Already screenshot'%TEXT)
        except NoSuchElementException, e:
            time.sleep(1)
          # print logger.info("Did not get to the control, click failed")
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.info('+FAIL+  not found"%s"element ??Already screenshot'%TEXT)
          # return True
    if method == "tag_name":
        try:
            emmm = self.driver.find_element_by_tag_name(TEXT)
            #self.assertIsNotNone(emm)
            logger.info('+PASS+  Find the"%s"element'%TEXT)
            emmm.click()
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  Click on the "%s" element to succeed??Already screenshot'%TEXT)
        except NoSuchElementException, e:
            time.sleep(1)
          # print logger.info("Did not get to the control, click failed")
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.info('+FAIL+  not found"%s"element ??Already screenshot'%TEXT)
          # return True
    if method == "xpath":
        try:
         #   WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(TEXT))
            emmm = self.driver.find_element_by_xpath(TEXT)
            #self.assertIsNotNone(emm)
            logger.info('+PASS+  Find the"%s"element'%TEXT)
            emmm.click()
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  Click on the "%s" element to succeed??Already screenshot'%TEXT)
        except NoSuchElementException, e:
            time.sleep(1)
          # print logger.info("Did not get to the control, click failed")
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print e
            print logger.info('+FAIL+  not found"%s"element ??Already screenshot'%TEXT)
          # return True
    if method == "calss_names":
        try:
            lis = self.driver.find_elements_by_class_name(TEXT)
            logger.info('+PASS+  Find the"%s"element'%TEXT)                            
            print lis[number].click()                  
            time.sleep(1)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  Click on the "%s" element to succeed??Already screenshot'%TEXT)
        except NoSuchElementException, e:
            time.sleep(1)
          # print logger.info("Did not get to the control, click failed")
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.info('+FAIL+  not found"%s"element ??Already screenshot'%TEXT)
          # return True
    if method == "elements_css_selector":
        try:
            lis = self.driver.find_elements_by_css_selector(TEXT)
            logger.info('+PASS+  Find the"%s"element'%TEXT)                            
            print lis[number].click()                  
            time.sleep(1)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  Click on the "%s" element to succeed??Already screenshot'%TEXT)
        except NoSuchElementException, e:
            time.sleep(1)
          # print logger.info("Did not get to the control, click failed")
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.info('+FAIL+  not found"%s"element ??Already screenshot'%TEXT)
          # return True
    if method == "elements_id":
        try:
            lis = self.driver.find_elements_by_id(TEXT)
            logger.info('+PASS+  Find the"%s"element'%TEXT)                            
            print lis[number].click()                  
            time.sleep(1)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  Click on the "%s" element to succeed??Already screenshot'%TEXT)
        except NoSuchElementException, e:
            time.sleep(1)
          # print logger.info("Did not get to the control, click failed")
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.info('+FAIL+  not found"%s"element ??Already screenshot'%TEXT)
          # return True
    if method == "elements_link_text":
        try:
            lis = self.driver.find_elements_by_link_text(TEXT)
            logger.info('+PASS+  Find the"%s"element'%TEXT)                            
            print lis[number].click()                  
            time.sleep(1)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  Click on the "%s" element to succeed??Already screenshot'%TEXT)
        except NoSuchElementException, e:
            time.sleep(1)
          # print logger.info("Did not get to the control, click failed")
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.info('+FAIL+  not found"%s"element ??Already screenshot'%TEXT)
          # return True
    if method == "elements_name":
        try:
            lis = self.driver.find_elements_by_name(TEXT)
            logger.info('+PASS+  Find the"%s"element'%TEXT)                            
            print lis[number].click()                  
            time.sleep(1)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  Click on the "%s" element to succeed??Already screenshot'%TEXT)
        except NoSuchElementException, e:
            time.sleep(1)
          # print logger.info("Did not get to the control, click failed")
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.info('+FAIL+  not found"%s"element ??Already screenshot'%TEXT)
          # return True
    if method == "elements_partial_link_text":
        try:
            lis = self.driver.find_elements_by_partial_link_text(TEXT)
            logger.info('+PASS+  Find the"%s"element'%TEXT)                            
            print lis[number].click()                  
            time.sleep(1)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  Click on the "%s" element to succeed??Already screenshot'%TEXT)
        except NoSuchElementException, e:
            time.sleep(1)
          # print logger.info("Did not get to the control, click failed")
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.info('+FAIL+  not found"%s"element ??Already screenshot'%TEXT)
          # return True
    if method == "elements_tag_name":
        try:
            lis = self.driver.find_elements_by_tag_name(TEXT)
            logger.info('+PASS+  Find the"%s"element'%TEXT)                            
            print lis[number].click()                  
            time.sleep(1)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  Click on the "%s" element to succeed??Already screenshot'%TEXT)
        except NoSuchElementException, e:
            time.sleep(1)
          # print logger.info("Did not get to the control, click failed")
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.info('+FAIL+  not found"%s"element ??Already screenshot'%TEXT)
          # return True
    if method == "elements_xpath":
        try:
            lis = self.driver.find_elements_by_xpath(TEXT)
            logger.info('+PASS+  Find the"%s"element'%TEXT)                            
            print lis[number].click()                  
            time.sleep(1)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  Click on the "%s" element to succeed??Already screenshot'%TEXT)
        except NoSuchElementException, e:
            time.sleep(1)
          # print logger.info("Did not get to the control, click failed")
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.info('+FAIL+  not found"%s"element ??Already screenshot'%TEXT)
          # return True
              