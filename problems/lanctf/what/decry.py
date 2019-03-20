'''
Created on Mar 20, 2019

@author: sherl
'''
from bitarray import bitarray,bitdiff
import numpy as np

def get_det_mod2(data, lend=256):
    if lend==2: return (data[0][0]*data[1][1]-data[1][0]*data[0][1])%2
    
    ret=0
    for i in range(lend):
        if lend==256: print i
        if data[0][i]:
            tep1=data[1:,:i]
            tep2=data[1:, (i+1):]
            next=np.concatenate([tep1,tep2],1)
            
            ret+=get_det_mod2(next, lend-1)
            ret%=2
    return ret


resu=b'83b98e262db120a1eb4e7bb527edf48d7f1daacb73671c96b45141aed2d583e7'


resu_bits=bitarray()
resu_bits.frombytes(resu.decode('hex'))


print len(resu_bits)
#print resu_bits

info=[]
with open('./info.txt','r') as f:
    for i in f.readlines():
        tep=i.strip()
        
        tt=bitarray()
        tt.frombytes(tep.decode('hex'))
        
        info.append(tt)


print len(info)
#for i in info: print len(i),i
print info[0]

#bitdiff(a, b)

matr=np.zeros([256,256], dtype=np.int64)

for ind,i in enumerate(info):
    for j in range(len(i)):
        if i[j]: matr[ind][j]=1

print matr.shape
print matr[0]

print get_det_mod2(matr)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

            

