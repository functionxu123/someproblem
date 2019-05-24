#coding:utf-8
'''
Created on May 24, 2019

@author: sherl
'''
import csv

csv_path=r'./device_failure.csv'



def read_csv(path=csv_path):
    map_id={}
    with open(path,  newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        for ind,row in enumerate(csvreader):
            #print (ind,row)
            key=row[1].strip()
            label=int(row[2])
            attrs=[int(i) for i in row[3:]]
            if key in map_id:
                map_id[key].append([attrs, label])
            else:
                map_id[key]=[[attrs, label]]
    return map_id
            
if __name__=='__main__':
    map_id=read_csv()
    
    cnt=0
    for ind,i in enumerate(map_id):
        print (ind, i, len(map_id[i]), map_id[i])
        cnt+=len(map_id[i])
    print (cnt)