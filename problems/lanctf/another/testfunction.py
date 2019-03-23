#coding:utf-8
'''
Created on 2019年3月24日

@author: sherl
'''
import math
from boto.sdb.db.sequence import double

R=4777053952827391 #/100
r=1940035480806554 #/100
a=62791383142154


t=(R**2) - (a**2)*100*25  #kai fang /100
print hex(a)[2:-1]

if __name__ == '__main__':
    pass