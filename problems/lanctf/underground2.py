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
tarurl=r'http://101.201.66.182:8012/admin'

strang_auth='username=test&role=user'
strang_sig=b'5b8f99d780ec542da912a5a5cf2bc341'


cookies={"auth": 'username=test&role=user'+'\x80'+'\x00'*25+'\x17'+'\x00'*7,#\role=admin&
         "sig": '\x51\xc5\x41\xa5\xa6\xa1\x7b\x50\xf2\x5a\xde\x01\x92\xa3\x3d\xfe'}
print (cookies)
print ((cookies['auth'][24]))

s=requests.session()


'''
r = s.get(tarurl,headers=headers, cookies=cookies) #


print (r.cookies)
print (r.status_code,r.text[:60])
'''

m = hashlib.md5()
auth_byte=unquote_to_bytes(cookies['auth'])
print ('after unquote len:',len(auth_byte))

print ((auth_byte))

m.update(auth_byte)
print (m.hexdigest())





if __name__ == '__main__':
    pass