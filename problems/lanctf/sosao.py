#coding:utf-8
'''
Created on Mar 21, 2019

@author: sherl
'''
from struct import *  

filp=r'/home/sherl/Downloads/ctf/misc/sosao'
st=0x000fb9
st2=0x167d
len=32
flag=''
kepstr=''


with open(filp, 'rb') as f:
    f.seek(st)
    
    for i in range(120):
        
        bt=f.read(2)
        if ord(bt[0])==0x89 and ord(bt[1])==0xf8:
            bt=f.read(1)
            if ord(bt)==0x81:
                kepstr='1'+kepstr
                bt=f.read(6)
            else:
                kepstr='0'+kepstr
                bt=f.read(5)
                
        
        
        if i%8==7:
            tepchr=chr ( int (kepstr, 2) )
            print tepchr
            flag+=tepchr
            kepstr=''
            
    print 'start seg2'
    flag+='u'
    f.seek(st2, 0)
    
    for i in range(260):
        
        bt=f.read(2)
        if ord(bt[0])==0x89 and ord(bt[1])==0xf8:
            bt=f.read(1)
            if ord(bt)==0x81:
                kepstr='1'+kepstr
                bt=f.read(6)
            else:
                kepstr='0'+kepstr
                bt=f.read(5)
                
        
        
        if i%8==7:
            tepchr=chr ( int (kepstr, 2) )
            print tepchr
            flag+=tepchr
            kepstr=''
print flag


if __name__ == '__main__':
    pass