#_*_coding:gb2312
import glob
import log,logging,gettime
from appium import webdriver
import unittest
import os,sys,time,re,xlrd
import HTMLTestRunner
from find import *
reload(sys)
sys.setdefaultencoding('GBK')
localpath = os.getcwd()
sys.path.append(localpath)
def load_tests():
    test_file_strings = glob.iglob(r'test_*.py')
    module_strings = [str[0:len(str)-3] for str in test_file_strings]
    #print module_strings
    caseList = '\n'.join(module_strings)
 #   print caseList
    suites = [unittest.defaultTestLoader.loadTestsFromName(str) for str in module_strings]
  #  print suites
    testSuite = unittest.TestSuite(suites)
  #  print testSuite
    return testSuite
  #  print logger.info(test_file_strings)
if __name__ == '__main__':
    try:
        if  gettime.EffectiveTime()==True:     #联网验证日期是否过期
            cleanEnv() # 清除件和新建文件 
            timestr = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
            filename ='result_'+ timestr + '.html'   
            fp =open(filename,'wb')
            runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'自动化测试报告',description=u'报告明细')
            runner.run(load_tests())
            #下面这句是原始的，不知道是什么意思，经过上面的改造，目前可以正常使用，且有报HTML报告输出
        #    unittest.TextTestRunner(verbosity=2).run(load_tests()) #
            fp.close()
            logging.shutdown()
            print '测试完成，详情请查看测试报告 %s'%filename
    except Exception,e:
        print e
    thisIsLove = raw_input('按 ENTER 键退出窗口！')