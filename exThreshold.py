import cv2,sys
import matplotlib.pyplot as plt
import myLib


src = imread('data2/apple_th.jpg',cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit('Image load failed')
    
myLib.hist_gray(src)

ret,src_th =cv2.threshold(src,230,255,cv2.THRESH_BINARY)
print(ret)
cv2.imshow('src',src)
cv2.imshow('src_th',src_th)
cv2.waitKey()
cv2.destroyAllWindows()    
# #src의 히스토그램을 가져오기
# hist =cv2.calcHist([src],[0],None,[256],[0.256])
# plt.plot(hist)
# plt.show()
    
#threshold 함수를 이용해서 흑과 백으로 나눈다
# src_th =cv2.threshold(src,127,255,cv2.THRESH_BINARY)

