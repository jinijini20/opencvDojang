import cv2,sys
import numpy as np
import matplotlib.pyplot as plt



#cartoon filter
src=cv2.imread('data2/noise1.jpg',cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit('IMage load failed')
    
    
dst = cv2.medianBlur(src,3)

cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.waitKey()
cv2.destroyAllWindows()