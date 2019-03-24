#coding:utf-8
'''
Created on 2019年3月24日

@author: sherl
'''
import math
import six

R=4777053952827391 #/100
r=1940035480806554 #/100
a=62791383142154


t=(R**2) - (a**2)*100*25  #kai fang /100
print hex(a)[2:-1]

def divide_find():
    cnt=0
    max_a=math.pi
    min_a=0
    alpha=(max_a+min_a)/2.0
    
    while alpha!=min_a and alpha!=max_a:
        print '\n',cnt
        print min_a, max_a,alpha
        
        up=a*(R*math.sin(alpha)+(t**0.5))
        
        tep1=2*(R**2) + a*100*R*math.cos(alpha) + 2*R*(t**0.5)*math.sin(alpha)
        tep2=2*(R**2) - a*100*R*math.cos(alpha) + 2*R*(t**0.5)*math.sin(alpha)
        down=a + ( (tep1**0.5) + (tep2**0.5) ) /100.0
        
        print up,down
        
        if up/down > r:
            max_a=alpha
        elif up/down<r:
            min_a=alpha
        else:
            print 'find it:',alpha
            break
        print 'diffs:',abs(up/down - r)
        alpha=(max_a+min_a)/2.0
        cnt+=1
        
    b=int((tep2**0.5)  /100.0)
    c=int( (tep1**0.5)/100.0 )
    print hex(b), hex(c)
    
divide_find()




