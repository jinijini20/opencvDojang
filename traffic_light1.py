import sys
import numpy as np
import cv2


#트랙바 콜백 함수 생성
def on_trackbar(pos):
    hmin = cv2.getTrackbarPos('H_min','Trackbar')
    hmax = cv2.getTrackbarPos('H_max','Trackbar')
    
    #inRange함수에 적용
    dst1 =cv2.inRange(src_hsv1,(hmin,150,0),(hmax,255,255))
    dst2 =cv2.inRange(src_hsv2,(hmin,150,0),(hmax,255,255))
    dst3 =cv2.inRange(src_hsv3,(hmin,150,0),(hmax,255,255))

#이미지 읽기
img1 = cv2.imread("data2/red.jpg")
img2 = cv2.imread("data2/yellow.jpg")
img3 = cv2.imread("data2/green.jpg")

if img1 is None:
    sys.exit("Image1 Load failed!")
if img2 is None:
    sys.exit("Image2 Load failed!")
if img3 is None:
    sys.exit("Image3 Load failed!")