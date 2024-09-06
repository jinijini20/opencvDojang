import cv2,sys
import numpy as np
import matplotlib.pyplot as plt



#cartoon filter
src=cv2.imread('data2/road.png',cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit('IMage load failed')
    
    
dst = cv2.Canny(src,64,128)

cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.waitKey()
cv2.destroyAllWindows()