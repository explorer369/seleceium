#_*_coding:GBK
import ntplib,os,datetime,time
def EffectiveTime():
    '''������֤��������
    '''
    # ���ù������ڣ�ע���ʽҪһ�£�
    ExpirationTime = '2016-08-09' 
    ExpirationTime = time.strptime(ExpirationTime,'%Y-%m-%d') #תΪ<type 'time.struct_time'>���͵ĸ�ʽ
    #��ȡ����ʱ��                 
    c = ntplib.NTPClient()
    try:
        response = c.request('pool.ntp.org')
        ts = response.tx_time
        _date = time.strftime('%Y-%m-%d',time.localtime(ts)) #�����2016-07-10
        _time = time.strftime('%X',time.localtime(ts))      #�����13:14:26    
        NetworkTime = time.strptime(_date,'%Y-%m-%d')  #��ȡ��ʱ��ΪstrתΪ<type 'time.struct_time'>
    except Exception,e:
        print e,'\n���������������' #\n��������ʾ���������
    #��ȡ����ϵͳʱ��
    SystemTime = time.strftime("%Y-%m-%d",time.localtime(time.time()))
    SystemTime = time.strptime(SystemTime,'%Y-%m-%d')
    try:
        if ExpirationTime > SystemTime and ExpirationTime > NetworkTime:
            return True
        elif ExpirationTime > NetworkTime:
            return True
        else:
            print '��֤���ڣ�����ϵ���ߣ�'
            return False            
    except (UnboundLocalError,Exception) as e:
        print e,'��֤���ڣ�����ϵ���ߣ�'
        return False