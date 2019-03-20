#coding:utf-8
'''
Created on Mar 15, 2019

@author: sherl
'''

from bitarray import bitarray
import base64

a='AnHZniLvmOHW1YJe5Sgdqgl\0:Ny0cHQcMBBcYOAQzVW5+VHwJClEzHlQ='
b='LiuBZYGvFfCi6HKmFkR"LZD\0:OiohBTM8DxczEQ8NUn9/XA8xPxcOI3w='
c='4kCKeIb3svqiOAjQZUaUNBQ\0:QigXDAwsKlIGAT0NK3ZeYBMPDGAMO2k='

d='OgIaBD0jMy4+KBULEWh/XyYtMm0NK0U='

kep_map={}   #key->encrypted char
positi_map={} #key->position

def process(strs):
    ori=strs.split(':')[0]
    encry=strs.split(':')[-1]
    tep_ori=bytes(ori)
    
    print ori[:-1]
    print encry  #31
    base64enc= base64.b64encode(ori) #32
    
    tep_bit_ori = bitarray(endian='big')
    tep_bit_ori.frombytes(tep_ori)
    #tep_bit_ori.reverse()

    
    for i in range(len(encry)):
        
        biti=bitarray('111111')
        
        
        if not kep_map.has_key(encry[i]):
            kep_map[encry[i]]=[  [i,tep_bit_ori[i*6:(i+1)*6] ]  ]
        else:
            kep_map[encry[i]].append([i,tep_bit_ori[i*6:(i+1)*6] ])
            
        
        if not positi_map.has_key(i):
            positi_map[i]=[ [tep_bit_ori[i*6:(i+1)*6] , encry[i],  base64enc[i]] ]  #ori  encry  base64encry
        else:
            positi_map[i].append( [tep_bit_ori[i*6:(i+1)*6] , encry[i], base64enc[i]]  )
        
            
        print i,encry[i],'-->',tep_bit_ori[i*6:(i+1)*6]

    return kep_map
        
        
process(a)
process(b)
process(c)


for i in kep_map:
    print '\n',i
    for j in kep_map[i]:
        print j

for i in positi_map:
    print '\n',i
    for j in positi_map[i]:
        print j


























