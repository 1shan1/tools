import cv2
import numpy as np

img1 = cv2.imread('/home/pengshanzhen/try/1.jpeg')
img2 = cv2.imread('/home/pengshanzhen/try/2.jpeg')

#img1 = np.array(img1)
#img2 = np.array(img2)

#print(img1)
#print(img2)
#exit()
img_mix = cv2.addWeighted(img1, 0.8, img2, 0.2, 0)
#print(img_mix)
#exit()
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img_mix', img_mix)

cv2.waitKey(0)
cv2.destroyAllWindows()
