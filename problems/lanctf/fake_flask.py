'''
Created on Mar 20, 2019

@author: sherl
'''

from flask import Flask
from urllib.parse import  *
import hashlib
from flask import request,make_response,redirect,url_for

SECRET=b'asdfdfg'



app=Flask(__name__) #创建1个Flask实例

@app.route('/')      #路由系统生成 视图对应url,1. decorator=app.route() 2. decorator(first_flask)
def hello():    #视图函数
    return 'Hello World'  #response

@app.route('/sdf')      #路由系统生成 视图对应url,1. decorator=app.route() 2. decorator(first_flask)
def hello2():    #视图函数
    return 'error'  #response

@app.route("/admin", methods=["GET"]) 
def admin_page(): 
    tep=request.cookies.get("auth")
    print ('get auth len',len(tep), tep)
    auth_cookie = unquote_to_bytes(tep) 
    sig_cookie = unquote_to_bytes(request.cookies.get("sig")) 
    
    print (len(auth_cookie),auth_cookie)
    print (len(sig_cookie), sig_cookie)
    
    if auth_cookie is None or sig_cookie is None: 
        print('one is none')
        return redirect(url_for("hello")) 
        
        
        
    if sig_cookie != make_signature(auth_cookie): 
        print ('not match:',sig_cookie ,make_signature(auth_cookie))
        resp = make_response(redirect(url_for("hello2"))) 
        resp.delete_cookie("auth") 
        resp.delete_cookie("sig") 
        return resp 
        
    print('passed')
    cookie_params = {} 
    for p in auth_cookie.split(b"&"): 
        print (p)
        key, val = p.split(b"=") 
        cookie_params[key] = val
    
    if cookie_params.get(b"role") == b"admin": 
        return 'FLAG_VALUE' 
    else: 
        return redirect(url_for("hello")) 
    
def make_signature(value): 
    temp = SECRET + value 
    print ('make sig:',len(temp), temp)
    temp=hashlib.md5(temp).hexdigest().encode()
    print (temp)
    return temp


if __name__ == '__main__':
    make_signature(b'username=test&role=user')
    app.run('127.0.0.1', 8012, True)              #启动socket
    
    
    
    
    