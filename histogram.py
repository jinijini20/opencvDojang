import cv2,sys
import numpy as np
import matplotlib.pyplot as plt

iscolor =True

if not isColor:
#grayscale
    src1=cv2.imread('data/Hawkes.jpg',cv2.IMREAD_GRAYSCALE)
    src2=cv2.imread('data/Hawkes_norm.jpg',cv2.IMREAD_GRAYSCALE)
    if src1 is None or src2 is None:
        sys.exit('Image load failed')
    


    
#히스토그램을 만들기
hist1=cv2.calcHist([src1],[0],[256],[0,256])
hist2=cv2.calcHist([src2],[0],[256],[0,256])

if iscolor:
    src =cv2.imread('data/lena.bmp')
    
    if src1  in None:
        sys.exit("Image Load failed")
        
    #컬러 채널 분리
    colors = ['b','g','r']
    bgr_planes = cv2.split(src)
    print(bgr_planes)

# cv2.imshow('src1',src1)
# # cv2.imshow('src2',src2)
# #matplotlib 띄우기
# plt.plot(hist1)
# plt.plot(hist2)
# plt.show()

cv2.waitkey() 
cv2.destroyAllWindows()
  