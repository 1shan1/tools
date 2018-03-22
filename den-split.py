import cv2  
import numpy  
import math  
import string  
import os  
import pandas as pd
import numpy as np


#path = '/home/pengshanzhen/try/1_1.jpg'
path ='/home/pengshanzhen/try/data/train_den/1_1.csv'

den = pd.read_csv(path,sep=',',header=None).as_matrix()
#print(den)
#print(den.shape)
#exit()
#den  = den.astype(np.float32, copy=False)
#img = cv2.imread(path)



ratio = 0.5
n = 4
#print(img)
dstPath ='/home/pengshanzhen/try/split_den/'
height = den.shape[0]  
width = den.shape[1]  
#cv2.imshow(imgPath, img)  
pHeight = int(ratio*height)  
pHeightInterval = (height-pHeight)/(n-1)  
      
#print 'pHeight: %d\n' %pHeight   
#print 'pHeightInterval: %d\n' %pHeightInterval  
      
pWidth = int(ratio*width)  
pWidthInterval = (width-pWidth)/(n-1)  
      
    #print 'pWidth: %d\n' %pWidth   
    #print 'pWidthInterval: %d\n' %pWidthInterval  
      
cnt = 1  
for i in range(n):  
    for j in range(n):  
        x = pWidthInterval * i  
        y = pHeightInterval * j  
              
        #print 'x: %d\n' %x  
        #print 'y: %d\n' %y  
              
        patch = den[y:y+pHeight, x:x+pWidth]  
        #print(patch)
        #print(patch.shape[0])
        #print(patch.shape[1])
        #print(patch[0][0])
        #exit()
        with open(dstPath+'_%d' %cnt+'.csv','w') as f :
          for h in range(patch.shape[0]):
            for l in range(patch.shape[1]):
              f.write(str(patch[h][l]))
              f.write(',')
            f.write('\n')



        #cv2.imwrite(dstPath+'_%d' %cnt+'.jpg', patch);  
        cnt += 1  
        #cv2.imshow('patch',patch)  
        #cv2.waitKey(0)  
      
