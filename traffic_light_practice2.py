import sys
import numpy as np
import cv2

def on_trackbar(pos):
    hmin =cv2.getTrackbarPos('H_min','Trackbar')
    hmax =cv2.getTrackbarPos('H_max','Trackbar')
    print(hmin,hmax)
    
    
mask_red1 = cv2.inRange(src_hsv,(0,100,0),(10,255,255))
mask_red2 = cv2.inRange(src_hsv,(160,100,0),(180,255,255))
mask_red =cv2.bitwise_or(mask_red1,mask_red2)

