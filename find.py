# -*- coding:GBK -*- 
import os,sys,time,re,subprocess,unittest
from ConfigParser import ConfigParser
import log,logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from  selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from distutils.cmd import Command
reload(sys)
sys.setdefaultencoding('GBK')
global driver,Testtime
localpath = os.getcwd()
sys.path.append(localpath)
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
cleanEnv() #让导入此文件时就执行清除件和新建文件(必须先要建文件后面的logging才可用)
# 读取配置文件
def config():
    configfile='config.txt' 
    config=ConfigParser()
    config.read(configfile)
    command = config.get('AssertionMode','command')
    return command
def is_chinese(uchar):

        """判断一个unicode是否是汉字"""

        if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
            #uchar.decode('gb2312').encode('utf-8')
            #uchar = uchar.decode('GBK')
            return uchar
        else:
            uchar = uchar.decode('GBK')
            return uchar
logger = log.Logger('rst/log.log',clevel = logging.DEBUG,Flevel = logging.INFO)
command = config()
print '当前断言方式为:%s'%command

def find_name(self,method,TEXT,number=0):
    def assertverify():
        '''处理断言是否继续执行和断言失败报告为FAIL
        '''
        if command == 'assert':
            self.assertEqual(111,TEXT,u'未找到:\"%s\"'%TEXT)
        elif command == 'verify':
            pass      
    Testtime=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    if method == "name":
        try:
            emmm = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_name(TEXT))
            #self.assertIsNotNone(emm) #这里也可以断言，不用下面异常下的断言其实也可以
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            emmm.click()
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  点击"%s"元素成功，已保存截图'%TEXT)
        except Exception, e:
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.error('+FAIL+  未找到"%s"元素， 已截图'%TEXT)
            assertverify()
    if method == "class_name":
        try:
            emmm = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_class_name(TEXT))
            #self.assertIsNotNone(emm)
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            emmm.click()
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  点击"%s"元素成功，已保存截图'%TEXT)
        except Exception, e:
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.error('+FAIL+  未找到"%s"元素， 已截图'%TEXT)
            assertverify()
    if method == "css":
        try:
            emmm = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_css_selector(TEXT))
            #self.assertIsNotNone(emm)
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            emmm.click()
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  点击"%s"元素成功，已保存截图'%TEXT)
        except Exception, e:
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.error('+FAIL+  未找到"%s"元素， 已截图'%TEXT)
            assertverify()
    
    if method == "id":
        try:
            emmm = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_id(TEXT))
            #self.assertIsNotNone(emm)
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            emmm.click()
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  点击"%s"元素成功，已保存截图'%TEXT)
        except Exception, e:
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.error('+FAIL+  未找到"%s"元素， 已截图'%TEXT)
            assertverify()
    if method == "link":
        try:
           # TEXT = is_chinese(TEXT)
            emmm = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_link_text(TEXT))
            #self.assertIsNotNone(emm)
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            emmm.click()
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  点击"%s"元素成功，已保存截图'%TEXT)
        except Exception, e:
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.error('+FAIL+  未找到"%s"元素，错误截图已保存'%TEXT)
            assertverify()
    if method == "partial_link":
        try:
            emmm = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_partial_link_text(TEXT))
            #self.assertIsNotNone(emm)
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            emmm.click()
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  点击"%s"元素成功，已保存截图'%TEXT)
        except Exception, e:
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.error('+FAIL+  未找到"%s"元素， 已截图'%TEXT)
            assertverify()
    if method == "tag":
        try:
            emmm = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_tag_name(TEXT))
            #self.assertIsNotNone(emm)
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            emmm.click()
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  点击"%s"元素成功，已保存截图'%TEXT)
        except Exception, e:
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.error('+FAIL+  未找到"%s"元素， 已截图'%TEXT)
            assertverify()
    if method == "xpath":
        try:
            emmm = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_xpath(TEXT))
            #self.assertIsNotNone(emm)
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            emmm.click()
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  点击"%s"元素成功，已保存截图'%TEXT)
        except Exception,e:      
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.error('+FAIL+  未找到"%s"元素， 已截图'%TEXT)
            assertverify()
    if method == "calss_names":
        try:
            lis = self.driver.find_elements_by_class_name(TEXT)
            logger.info('+PASS+  找到"%s"元素'%TEXT)                            
            print lis[number].click()                  
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  点击"%s"元素成功，已保存截图'%TEXT)
        except Exception, e:
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.error('+FAIL+  未找到"%s"元素， 已截图'%TEXT)
            assertverify()
    if method == "elements_css":
        try:
            lis = self.driver.find_elements_by_css_selector(TEXT)
            logger.info('+PASS+  找到"%s"元素'%TEXT)                            
            print lis[number].click()                  
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  点击"%s"元素成功，已保存截图'%TEXT)
        except Exception, e:
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.error('+FAIL+  未找到"%s"元素， 已截图'%TEXT)
            assertverify()
    if method == "elements_id":
        try:
            lis = self.driver.find_elements_by_id(TEXT)
            logger.info('+PASS+  找到"%s"元素'%TEXT)                            
            print lis[number].click()                  
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  点击"%s"元素成功，已保存截图'%TEXT)
        except Exception, e:
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.error('+FAIL+  未找到"%s"元素， 已截图'%TEXT)
            assertverify()
    if method == "elements_link":
        try:
            lis = self.driver.find_elements_by_link_text(TEXT)
            logger.info('+PASS+  找到"%s"元素'%TEXT)                            
            print lis[number].click()                  
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  点击"%s"元素成功，已保存截图'%TEXT)
        except Exception, e:
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.error('+FAIL+  未找到"%s"元素， 已截图'%TEXT)
            assertverify()
    if method == "elements_name":
        try:
            lis = self.driver.find_elements_by_name(TEXT)
            logger.info('+PASS+  找到"%s"元素'%TEXT)                            
            print lis[number].click()                  
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  点击"%s"元素成功，已保存截图'%TEXT)
        except Exception, e:
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.error('+FAIL+  未找到"%s"元素， 已截图'%TEXT)
            assertverify()
    if method == "elements_partial_link":
        try:
            lis = self.driver.find_elements_by_partial_link_text(TEXT)
            logger.info('+PASS+  找到"%s"元素'%TEXT)                            
            print lis[number].click()                  
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  点击"%s"元素成功，已保存截图'%TEXT)
        except Exception, e:
            time.sleep(1)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.error('+FAIL+  未找到"%s"元素， 已截图'%TEXT)
            assertverify()
    if method == "elements_tag":
        try:
            lis = self.driver.find_elements_by_tag_name(TEXT)
            logger.info('+PASS+  找到"%s"元素'%TEXT)                            
            print lis[number].click()                  
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  点击"%s"元素成功，已保存截图'%TEXT)
        except Exception, e:
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.error('+FAIL+  未找到"%s"元素， 已截图'%TEXT)
            assertverify()
    if method == "elements_xpath":
        try:
            lis = self.driver.find_elements_by_xpath(TEXT)
            logger.info('+PASS+  找到"%s"元素'%TEXT)                            
            print lis[number].click()                  
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  点击"%s"元素成功，已保存截图'%TEXT)
        except Exception, e:
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.error('+FAIL+  未找到"%s"元素， 已截图'%TEXT)
            assertverify()
      