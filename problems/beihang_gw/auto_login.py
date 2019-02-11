#coding:utf-8
'''
Created on May 10, 2018

@author: root
'''
import urllib
import base64
import urllib2,time
from datetime import datetime

cookie_1=""
cookie_2=""

def send_post(username, passwd):
    global cookie_1,cookie_2
    test_data = "action=login&username="+username+\
                "&password={B}"+passwd+\
                "&ac_id=20"+\
                "&user_ip="+""+\
                "&nas_ip="+""+\
                "&user_mac="+""+\
                "&save_me="+"0"+\
                "&ajax=1"
    test_data_urlencode = test_data  #urllib.urlencode(test_data)
    
    requrl = "https://gw.buaa.edu.cn:803/include/auth_action.php"
    
    #浏览器伪装
    user_agent = r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    headers={'User-Agent':user_agent}
    '''
    #添加cookie
    kep_cookie=""
    if (len(cookie_1)>0):
        kep_cookie+="double_stack_login="+cookie_1
    if (len(cookie_2)>0):
        kep_cookie+=";login="+cookie_2
    '''
    
    req = urllib2.Request(url = requrl,data =test_data_urlencode, headers=headers)
    
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    if (res.split(',')[0].strip()=="login_ok"):
        cookie_1=res.split(',')[1].strip()
        cookie_2=res.split(',')[2].strip()
        
    return  res
'''
    Request URL: https://gw.buaa.edu.cn:803/include/auth_action.php
Request Method: POST
Status Code: 200 OK
Remote Address: 10.200.21.4:803
Referrer Policy: no-referrer-when-downgrade
Connection: Keep-Alive
Content-Type: text/html
Date: Mon, 11 Feb 2019 10:15:15 GMT
Keep-Alive: timeout=1, max=250
Server: Apache/2.4.12 (Unix) OpenSSL/1.0.1g-fips PHP/5.5.23
Set-Cookie: login=bQ0pOyR6IXU7PJaQQqRAcBPxGAvxAcrglI630SCO%252BUcef0K8w8uumhuMp067TALwZYrSC1fkHKgPAxt5nRJL1r3xSGtZVzh0987s2CLseP2FAhBVYGjTZqWbATFG6LKijqHz1KhCWdQUQmTJJpXMnCxZSKW6HmTfowrkpQGWfYIJOdTVz%252Bqmxqui%252BlpO6JFWAzBY%252BsZePCywBOlP3dq7%252FExCjS6yrXyaAjUhrdMrswCZoeLlfXc3LxY%253D; expires=Wed, 13-Mar-2019 10:15:15 GMT; Max-Age=2592000
Transfer-encoding: chunked
X-Powered-By: PHP/5.5.23
Accept: */*
Accept-Encoding: gzip, deflate, br
Accept-Language: zh,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7
Connection: keep-alive
Content-Length: 113
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Cookie: login=bQ0pOyR6IXU7PJaQQqRAcBPxGAvxAcrglI630SCO%252BUcef0K8w8uumhuMp067TALwZYrSC1fkHKgPAxt5nRJL1r3xSGtZVzh0987s2CLseP2FAhBVYGjTZqWbATFG6LKijqHz1KhCWdQUQmTJJpXMnCxZSKW6HmTfowrkpQGWfYIJOdTVz%252Bqmxqui%252BlpO6JFWAzBY%252BsZePCywBOlP3dq7%252FExCjS6yrXyaAjUhrdMrswCZoeLlfXc3LxY%253D; cookie=83282749; login=bQ0pOyR6IXU7PJaQQqRAcBPxGAvxAcrglI630SCO%252BUcef0K8w8uumhuMp067TALwZYrSC1fkHKgPAxt5nRJL1r3xSGtZVzh0987s2CLseP2FAhBVYGjTZqWbATFG6LKijqHz1KhCWdQUQmTJJpXMnCxZSKW6HmTfowrkpQGWfYIJOdTVz%252Bqmxqui%252BlpO6JFWAzBY%252BsZePCywBOlP3dq7%252FExCjS6yrXyaAjUhrdMrswCZoeLlfXc3LxY%253D; PHPSESSID=iubp402amptp012out3g5nf4l2
Host: gw.buaa.edu.cn:803
Origin: https://gw.buaa.edu.cn:803
Referer: https://gw.buaa.edu.cn:803/beihanglogin.php?ac_id=20&url=http://gw.buaa.edu.cn:803/beihangview.php
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
X-Requested-With: XMLHttpRequest
action: login
username: zy1706333
password: {B}dGFvYmFvMg==
ac_id: 20
user_ip: 
nas_ip: 
user_mac: 
save_me: 0
ajax: 1
'''






if __name__ == '__main__':
    username="zy1706333"
    passwd="dGFvYmFvMg=="
    
    while (1):
        resu=send_post(username, passwd)
        
        TIMESTAMP = "{0:%Y-%m-%d_%H-%M-%S}".format(datetime.now())
        print (TIMESTAMP+"-->"+resu+'\n')
        if (resu.split(',')[0].strip()=="login_ok"):        time.sleep(60*60*2)
        else: time.sleep(5)
    
    
    
    
    