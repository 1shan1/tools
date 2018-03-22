import cv2  
import numpy  
import math  
import string  
import os  




path = '/home/pengshanzhen/try/1_1.jpg'
#den_path ='/home/pengshanzhen/try/data/train_den/1_1.csv'

#den = pd.read_csv(label_path,sep=',',header=None).as_matrix()
#den  = den.astype(np.float32, copy=False)
img = cv2.imread(path)

print(img)
print(img.shape)
exit()


ratio = 0.5
n = 4
#print(img)
dstPath ='/home/pengshanzhen/try/split_img/'
height = img.shape[0]  
width = img.shape[1]  
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
              
        patch = img[y:y+pHeight, x:x+pWidth, :]  
        cv2.imwrite(dstPath+'_%d' %cnt+'.jpg', patch);  
        cnt += 1  
        #cv2.imshow('patch',patch)  
        #cv2.waitKey(0)  
      
