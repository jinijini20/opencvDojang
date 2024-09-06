import cv2,sys
import numpy as np
import matplotlib.pyplot as plt



#cartoon filter
src=cv2.imread('data/lena.bmp')

if src is None:
    sys.exit('IMage load failed')
    
    
dst = cv2.bilateralFilter(src,-1,10,5)

cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.waitKey()
cv2.destroyAllWindows()