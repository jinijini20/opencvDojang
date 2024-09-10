import cv2,sys
import numpy as np

img2=cv2.imread('mission7.jpg')

if img2 is None:
    print('Image load failed')
    
    
blurred_img = cv2.GaussianBlur(img2,(5,5),0)

resized_area1 = cv2.resize(img2,(128,128),interpolation=cv2.INTER_AREA)
resized_linear = cv2.resize(img2,(128,128),interpolation=cv2.INTER_LINEAR)
resized_area3 = cv2.resize(blurred_img,(128,128),interpolation=cv2.INTER_AREA)

cv2.imwrite('inter_area_only.jpg',resized_area1)
cv2.imwrite('inter_area_only.jpg',resized_linear)
cv2.imwrite('inter_area_only.jpg',resized_area3)