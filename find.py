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
    '''ÿ��ִ������ʱ�ͰѴ�rstĿ¼ɾ��,Ȼ�����½�rst,�൱������ϴεĲ��Խ������־
    '''                        
    os.system('adb kill-server')
    needClean = ['log.log','img','rst']   # ������=log.log,img,rst������ֵ
    pwd = os.getcwd()                     # pwd=��ǰ�ļ�Ŀ¼
    for i in needClean:                   # ѭ��needClean
        delpath = os.path.join(pwd,i)     # ���Ϊ����ǰĿ¼\img�͵�ǰĿ¼\rst  ������C:\Users\Administrator\Desktop\���Խ��\img��
        if os.path.isfile(delpath):
            cmd = 'del /f/s/q "%s"'% delpath   # ɾ��delpath�õ��������ļ��У�img��rst��/F ǿ��ɾ��ֻ���ļ�/S ��������Ŀ¼ɾ��ָ���ļ�/Q ����ģʽ��ɾ��ȫ��ͨ���ʱ����Ҫ��ȷ�ϡ�
            os.system(cmd)
        elif os.path.isdir(delpath):       # ����ɾ��delpath�õ��������ļ��У�img��rst��
            cmd = 'rd /s/q "%s"' %delpath
            os.system(cmd)
    if not os.path.isdir('rst/screenshot'):
     #   os.makedirs('rst')          
        os.makedirs('rst/screenshot/Failed')
        os.makedirs('rst/screenshot/Passed')
cleanEnv() #�õ�����ļ�ʱ��ִ����������½��ļ�(������Ҫ���ļ������logging�ſ���)
# ��ȡ�����ļ�
def config():
    configfile='config.txt' 
    config=ConfigParser()
    config.read(configfile)
    command = config.get('AssertionMode','command')
    return command
def is_chinese(uchar):

        """�ж�һ��unicode�Ƿ��Ǻ���"""

        if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
            #uchar.decode('gb2312').encode('utf-8')
            #uchar = uchar.decode('GBK')
            return uchar
        else:
            uchar = uchar.decode('GBK')
            return uchar
logger = log.Logger('rst/log.log',clevel = logging.DEBUG,Flevel = logging.INFO)
command = config()
print '��ǰ���Է�ʽΪ:%s'%command

def find_name(self,method,TEXT,number=0):
    def assertverify():
        '''��������Ƿ����ִ�кͶ���ʧ�ܱ���ΪFAIL
        '''
        if command == 'assert':
            self.assertEqual(111,TEXT,u'δ�ҵ�:\"%s\"'%TEXT)
        elif command == 'verify':
            pass      
    Testtime=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    if method == "name":
        try:
            emmm = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_name(TEXT))
            #self.assertIsNotNone(emm) #����Ҳ���Զ��ԣ����������쳣�µĶ�����ʵҲ����
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            emmm.click()
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  ���"%s"Ԫ�سɹ����ѱ����ͼ'%TEXT)
        except Exception, e:
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.error('+FAIL+  δ�ҵ�"%s"Ԫ�أ� �ѽ�ͼ'%TEXT)
            assertverify()
    if method == "class_name":
        try:
            emmm = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_class_name(TEXT))
            #self.assertIsNotNone(emm)
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            emmm.click()
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  ���"%s"Ԫ�سɹ����ѱ����ͼ'%TEXT)
        except Exception, e:
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.error('+FAIL+  δ�ҵ�"%s"Ԫ�أ� �ѽ�ͼ'%TEXT)
            assertverify()
    if method == "css":
        try:
            emmm = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_css_selector(TEXT))
            #self.assertIsNotNone(emm)
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            emmm.click()
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  ���"%s"Ԫ�سɹ����ѱ����ͼ'%TEXT)
        except Exception, e:
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.error('+FAIL+  δ�ҵ�"%s"Ԫ�أ� �ѽ�ͼ'%TEXT)
            assertverify()
    
    if method == "id":
        try:
            emmm = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_id(TEXT))
            #self.assertIsNotNone(emm)
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            emmm.click()
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  ���"%s"Ԫ�سɹ����ѱ����ͼ'%TEXT)
        except Exception, e:
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.error('+FAIL+  δ�ҵ�"%s"Ԫ�أ� �ѽ�ͼ'%TEXT)
            assertverify()
    if method == "link":
        try:
           # TEXT = is_chinese(TEXT)
            emmm = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_link_text(TEXT))
            #self.assertIsNotNone(emm)
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            emmm.click()
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  ���"%s"Ԫ�سɹ����ѱ����ͼ'%TEXT)
        except Exception, e:
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.error('+FAIL+  δ�ҵ�"%s"Ԫ�أ������ͼ�ѱ���'%TEXT)
            assertverify()
    if method == "partial_link":
        try:
            emmm = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_partial_link_text(TEXT))
            #self.assertIsNotNone(emm)
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            emmm.click()
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  ���"%s"Ԫ�سɹ����ѱ����ͼ'%TEXT)
        except Exception, e:
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.error('+FAIL+  δ�ҵ�"%s"Ԫ�أ� �ѽ�ͼ'%TEXT)
            assertverify()
    if method == "tag":
        try:
            emmm = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_tag_name(TEXT))
            #self.assertIsNotNone(emm)
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            emmm.click()
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  ���"%s"Ԫ�سɹ����ѱ����ͼ'%TEXT)
        except Exception, e:
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.error('+FAIL+  δ�ҵ�"%s"Ԫ�أ� �ѽ�ͼ'%TEXT)
            assertverify()
    if method == "xpath":
        try:
            emmm = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_xpath(TEXT))
            #self.assertIsNotNone(emm)
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            emmm.click()
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  ���"%s"Ԫ�سɹ����ѱ����ͼ'%TEXT)
        except Exception,e:      
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.error('+FAIL+  δ�ҵ�"%s"Ԫ�أ� �ѽ�ͼ'%TEXT)
            assertverify()
    if method == "calss_names":
        try:
            lis = self.driver.find_elements_by_class_name(TEXT)
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)                            
            print lis[number].click()                  
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  ���"%s"Ԫ�سɹ����ѱ����ͼ'%TEXT)
        except Exception, e:
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.error('+FAIL+  δ�ҵ�"%s"Ԫ�أ� �ѽ�ͼ'%TEXT)
            assertverify()
    if method == "elements_css":
        try:
            lis = self.driver.find_elements_by_css_selector(TEXT)
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)                            
            print lis[number].click()                  
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  ���"%s"Ԫ�سɹ����ѱ����ͼ'%TEXT)
        except Exception, e:
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.error('+FAIL+  δ�ҵ�"%s"Ԫ�أ� �ѽ�ͼ'%TEXT)
            assertverify()
    if method == "elements_id":
        try:
            lis = self.driver.find_elements_by_id(TEXT)
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)                            
            print lis[number].click()                  
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  ���"%s"Ԫ�سɹ����ѱ����ͼ'%TEXT)
        except Exception, e:
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.error('+FAIL+  δ�ҵ�"%s"Ԫ�أ� �ѽ�ͼ'%TEXT)
            assertverify()
    if method == "elements_link":
        try:
            lis = self.driver.find_elements_by_link_text(TEXT)
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)                            
            print lis[number].click()                  
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  ���"%s"Ԫ�سɹ����ѱ����ͼ'%TEXT)
        except Exception, e:
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.error('+FAIL+  δ�ҵ�"%s"Ԫ�أ� �ѽ�ͼ'%TEXT)
            assertverify()
    if method == "elements_name":
        try:
            lis = self.driver.find_elements_by_name(TEXT)
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)                            
            print lis[number].click()                  
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  ���"%s"Ԫ�سɹ����ѱ����ͼ'%TEXT)
        except Exception, e:
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.error('+FAIL+  δ�ҵ�"%s"Ԫ�أ� �ѽ�ͼ'%TEXT)
            assertverify()
    if method == "elements_partial_link":
        try:
            lis = self.driver.find_elements_by_partial_link_text(TEXT)
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)                            
            print lis[number].click()                  
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  ���"%s"Ԫ�سɹ����ѱ����ͼ'%TEXT)
        except Exception, e:
            time.sleep(1)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.error('+FAIL+  δ�ҵ�"%s"Ԫ�أ� �ѽ�ͼ'%TEXT)
            assertverify()
    if method == "elements_tag":
        try:
            lis = self.driver.find_elements_by_tag_name(TEXT)
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)                            
            print lis[number].click()                  
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  ���"%s"Ԫ�سɹ����ѱ����ͼ'%TEXT)
        except Exception, e:
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.error('+FAIL+  δ�ҵ�"%s"Ԫ�أ� �ѽ�ͼ'%TEXT)
            assertverify()
    if method == "elements_xpath":
        try:
            lis = self.driver.find_elements_by_xpath(TEXT)
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)                            
            print lis[number].click()                  
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  ���"%s"Ԫ�سɹ����ѱ����ͼ'%TEXT)
        except Exception, e:
            time.sleep(1.5)
            self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
            print logger.error('+FAIL+  δ�ҵ�"%s"Ԫ�أ� �ѽ�ͼ'%TEXT)
            assertverify()
      