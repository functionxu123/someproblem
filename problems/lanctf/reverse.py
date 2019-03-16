#coidng:utf-8
'''
Created on Mar 16, 2019

@author: sherl
'''

from struct import *  
import numpy as np
import math

########################################################################
filpath=r'/home/sherl/Downloads/ctf/Moss-pwd-e5cd484b2206c837770d2467c3dc767f/MossTerminal'
len=16
st=0x2080
st2=0x2480

#################################################################################
matric=np.mat(np.zeros([len,len]))
resu1=np.mat(np.zeros([len]))
resu2=np.mat(np.zeros([len]))

print (matric.shape, resu1.shape)

with open(filpath, 'rb') as f:
    f.seek(st)
    for i in range(len):
        for j in range(len):
            tep=unpack('i', f.read(4))[0]
            print (tep,matric[i,j])
            matric[i,j]=tep
    f.seek(st2)
    for i in range(len):
        tep=unpack('i', f.read(4))[0]
        print (tep, resu1[0,i])
        resu1[0,i]=tep
    for i in range(len):
        tep=unpack('i', f.read(4))[0]
        print (tep, resu2[0,i])
        resu2[0,i]=tep
        
def get_str_from_mat(matric, vec):

    resver_resu=matric.I * vec.T
    resver_resu=np.array(resver_resu.T)
    print (resver_resu.shape)
    li=[]
    for i in resver_resu[0]:
        print (i)
        tepi=int( round(i)) 
        print (tepi, chr(tepi))
        li.append(chr(tepi))
    return ''.join(li)
    
print (get_str_from_mat(matric, resu1))
print (get_str_from_mat(matric, resu2))
    
    
    
    
    
