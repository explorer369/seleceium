#_*_coding:gb2312
import log,logging,gettime,glob,unittest
from appium import webdriver
import os,sys,time,re,xlrd
import HTMLTestRunner # ���ʹ��GBK���� 766��772��Ϊ��Ӧ�ı����ʽ
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
        if  gettime.EffectiveTime()==True:     #������֤�����Ƿ����
            timestr = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
            filename ='result_'+ timestr + '.html'   
            fp =open(filename,'wb')
            runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'�Զ������Ա���',description=u'������ϸ')
            runner.run(load_tests())
            #���������ԭʼ�ģ���֪����ʲô��˼����������ĸ��죬Ŀǰ��������ʹ�ã����б�HTML�������
        #    unittest.TextTestRunner(verbosity=2).run(load_tests()) #
            fp.close()
            logging.shutdown()
            print '������ɣ�������鿴���Ա��� %s'%filename
    except Exception,e:
        print e
    thisIsLove = raw_input('�� ENTER ���˳����ڣ�')