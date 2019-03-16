#coding:utf-8
'''
Created on Mar 15, 2019

@author: sherl
'''

from bitarray import bitarray

a='AnHZniLvmOHW1YJe5Sgdqgl\0:Ny0cHQcMBBcYOAQzVW5+VHwJClEzHlQ'
b='LiuBZYGvFfCi6HKmFkR"LZD\0:OiohBTM8DxczEQ8NUn9/XA8xPxcOI3w'
c='4kCKeIb3svqiOAjQZUaUNBQ\0:QigXDAwsKlIGAT0NK3ZeYBMPDGAMO2k'

d='OgIaBD0jMy4+KBULEWh/XyYtMm0NK0U'

kep_map={}

def process(strs):
    ori=strs.split(':')[0]
    encry=strs.split(':')[-1]
    tep_ori=bytes(ori)
    
    print ori
    print encry
    
    tep_bit_ori = bitarray(endian='big')
    tep_bit_ori.frombytes(tep_ori)
    #tep_bit_ori.reverse()
    
    
    for i in range(len(encry)):
        kep_map[encry[i]]=tep_bit_ori[i*6:(i+1)*6]
        print i,encry[i],'-->',tep_bit_ori[i*6:(i+1)*6]
        
process(a)
process(b)
process(c)

print len(kep_map)

tta=bitarray()
for i in d:
    tta.append(kep_map[i])

print tta.tobytes()