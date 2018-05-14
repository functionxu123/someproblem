#coding:utf-8
'''
Created on May 14, 2018

@author: root
'''
import cv2,os
import os.path as op
import numpy as np
import random,math
from random import randint

screen=[720,1024,3]
#screen_border=100#the video generate area

round_r=200

video_initlen=100#the video's length and width at it's just appeared
video_endlen=20#the video's... when it's move at end


indir=r'/media/sherl/本地磁盘/wokmaterial/ruizhi/BKVideos/neg_500'
outfile=r'demo.mp4'

paths=list(map(lambda x:op.join(indir,x),os.listdir(indir)))
random.shuffle(paths)

video_cnt=len(paths)
video_per=1#how many video appear per time

time_move_all=1.5
time_all=10.0#all time from start to end
time_generate_gap=(time_all-time_move_all-0.1)/video_cnt/video_per#
fps=60.0



class VideoMove(object):
    def __init__(self,path):
        capture=cv2.VideoCapture(path)
        #print 'frame:',int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        
        self.cap=capture
        self.framcnt=capture.get(cv2.CAP_PROP_FRAME_COUNT)-2  # 总帧数
        
        self.stx=video_initlen/2+float(random.randint(0,screen[1]-1-int(video_initlen)))
        self.sty=video_initlen/2+float(random.randint(0,screen[0]-1-int(video_initlen)))
        
        tep=random.randint(0,3)
        if tep==0: 
            self.sty=video_initlen/2.0

        elif tep==1:self.stx=screen[1]-video_initlen/2.0
        elif tep==2: self.sty=screen[0]-video_initlen/2.0
        else: self.stx=video_initlen/2.0
        
        self.curx=self.stx
        self.cury=self.sty
        
        #print 'inint stx;',self.stx, self.sty
        
        angle=randint(0,360)
        rr=random.random()*round_r
        self.endx=screen[1]/2+rr*math.cos(angle)
        self.endy=screen[0]/2+rr*math.sin(angle)
        
        
        self.timecnt=0
        
    def __del__(self):
        self.cap.release()
        
    def step(self):
        self.timecnt+=1/fps
        
    def show(self,npar):
        teprate=self.timecnt/time_move_all
        
        if teprate>1: teprate=1
        
        self.curx=self.stx+int((self.endx-self.stx)*teprate)
        self.cury=self.sty+int((self.endy-self.sty)*teprate)
        
        
        
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, int(teprate*self.framcnt))
        success, frame = self.cap.read()  # 循环读取下一帧          
        if success:        
            teplen=video_initlen-int((video_initlen-video_endlen)*teprate)
            res=cv2.resize(frame,(teplen,teplen))
            #cv2.imshow('tt',res)
            teplendiv2=int(teplen/2)
            tepstx=int(self.curx)-teplendiv2
            
            tepsty=int(self.cury)-teplendiv2
           
            #print res[0][0]
            
            npar[tepsty:tepsty+teplen,tepstx:tepstx+teplen,:]=res[:,:,:]
            #print npar[tepsty][tepstx]
        
def startdemo():
    kep_obj=[]  
    
    time_cnt=0
    
    video_writer = cv2.VideoWriter(outfile,
                    -1,#cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
                    fps,
                    (screen[0],screen[1]))
    
    while(time_cnt<time_all):
        print "schedule:",int(100*time_cnt/time_all),'%'
        kep=np.zeros(screen,dtype=np.uint8)
        #print kep.shape
        
        time_cnt+=1/fps
        tl=int(time_cnt/time_generate_gap*video_per)
        if tl>len(paths): tl=len(paths)
        for i in range(len(kep_obj),tl):
            kep_obj.append(VideoMove(paths[i]))
        for i in kep_obj:
            i.show(kep)
            i.step()
            
        #kep[:,:,0],kep[:,:,2]=kep[:,:,2],kep[:,:,0]
        #print kep
        video_writer.write(kep)
        cv2.imshow('test',kep)
        cv2.waitKey(1) #int(1/fps*1000)
    
    video_writer.release()
                

if __name__ == '__main__':
    startdemo()











