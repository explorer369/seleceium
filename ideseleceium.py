'''
Created on 2016-6-23

@author: Administrator
'''
#conding:utf-8
from selenium import webdriver
import unittest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome(executable_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe")
#browser.get("http://m12308.f3322.net:8070/login.html")
time.sleep(5)
class Sss(unittest.TestCase):
    def setUp(self):
        self.driver = browser
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_sss(self):
        driver = self.driver
        driver.get(self.base_url + "/s?ie=utf-8&f=3&rsv_bp=0&rsv_idx=1&tn=baidu&wd=sss&rsv_pq=f2c85050000ac46c&rsv_t=ccebKPKUJyojR1vdXdmPXXpjIl4b04q0Ec7QXSgsKTKmpFoo1ZbGf9qQvm0&rqlang=cn&rsv_enter=0&rsv_sug3=3&rsv_sug1=1&rsv_slog=btn_click&rsp=0&rsv_sug4=2644")
        driver.find_element_by_id("kw").click()
        driver.find_element_by_id("kw").click()
        driver.find_element_by_id("su").click()
        driver.find_element_by_id("su").click()
    
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