import skvideo
import skvideo.io
import cv2
import os


videogen = skvideo.io.vread('/media/pengshanzhen/bb42233c-19d1-4423-b161-e5256766be8e/video/Video2/1516069715.avi')
frame_path = '/media/pengshanzhen/bb42233c-19d1-4423-b161-e5256766be8e/video/Video2/1516069715.frame'



for i in range(len(videogen)):
   
  frame_name =str(i)+'.jpg' 
  cv2.imwrite(str(os.path.join(frame_path,frame_name)),videogen[i])
  
  
  
