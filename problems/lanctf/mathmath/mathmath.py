#!/usr/bin/env python2
#coding:utf-8
'''
Created on Mar 20, 2019

@author: sherl
'''

from pwn import *
import base64
import libnum

BLOCK_SIZE = 32
p = remote("101.201.66.182",1341)
#p = remote("127.0.0.1",1341)

def xor(number):
    p.sendafter("you can choose what you want here\n","xor")
    p.sendafter("send how long the number you want to xor\n",str(len(str(number))).rjust(4,"0"))
    p.sendafter("send the number you want to xor\n",str(number))
    return p.recvline()

def add(number):
    p.sendafter("you can choose what you want here\n","add")
    p.sendafter("send how long the number you want to add\n",str(len(str(number))).rjust(4,"0"))
    p.sendafter("send the number you want to add\n",str(number))
    return p.recvline()

def guess_key(key):
    p.sendafter("you can choose what you want here\n","ppp")
    p.recvuntil("you got a magic\n")
    p.send(key)
    info = p.recvline()
    if info == "OH!How do you get it\n":
        return p.recv()
    else:
        return False

def xor_add_oracle():
    """
    your code here to judge the amazing key
    """
    str=''
    for  i in range(32*8):
        num=2**i
        print i,'-->',num,'hex repentation:',hex(num)
        if xor(num)==add(num):
            str='0'+str
        else: str='1'+str
    
    print len(str),str
    resu= int(str, 2)
    
    print resu
    print 'result1:',hex(resu)
    resu=hex(resu)[2:].decode('hex')
    
    
    
    print type(resu),resu
    print guess_key( resu )
    
    
    '''
    str='1'+str[1:]
    resu= int(str,2)
    print 'result2:',hex(resu) 
    
    resu= bytes(resu)
    print guess_key(resu)
    '''
    

xor_add_oracle()

p.close()