#coding:utf-8
'''
Created on May 10, 2018

@author: root
'''

m1=['I','X','C','M']
m5=['V','L','D']


def generate(numd,cnt=0):
    if not numd:
        return ''
    
    maxd=numd%10
    
    if maxd<=3:
        resu=m1[cnt]*maxd
    elif maxd==4:
        resu=m1[cnt]+m5[cnt]
    elif maxd<9:
        resu=m5[cnt]+m1[cnt]*(maxd-5)
    else:
        resu=m1[cnt]+m1[cnt+1]
    
    return generate(int(numd/10),cnt+1)+resu

if __name__ == '__main__':
    print generate(3999)