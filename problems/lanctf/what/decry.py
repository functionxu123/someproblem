'''
Created on Mar 20, 2019

@author: sherl
'''
from bitarray import bitarray

resu=b'83b98e262db120a1eb4e7bb527edf48d7f1daacb73671c96b45141aed2d583e7'


resu_bits=bitarray()
resu_bits.frombytes(resu.decode('hex'))


print len(resu_bits)
print resu_bits

info=[]
with open('/home/sherl/Downloads/ctf/web/whatisthat/info.txt','r') as f:
    for i in f.readlines():
        tep=i.strip()
        
        tt=bitarray()
        tt.frombytes(tep.decode('hex'))
        
        info.append(tt)



for i in info: print len(i),i


