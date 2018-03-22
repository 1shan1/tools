import os
import cv2
import skvideo
import skvideo.io
import cv2
import os
import numpy as np




#videogen = skvideo.io.vread('/home/pengshanzhen/try/video2_1516067588.avi')
cap = cv2.VideoCapture('/home/pengshanzhen/try/video2_1516067588.avi')  
frame_path = '/home/pengshanzhen/try/1/'


i=0
while(True):
   
      ret, frame = cap.read()

      frame = frame.astype(np.float32, copy=False)
      frame_name =str(i)+'.jpg' 
      cv2.imwrite(str(os.path.join(frame_path,frame_name)),frame)
      i = i +1
  
