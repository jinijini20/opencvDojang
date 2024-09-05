import cv2,sys

#이미지 불러오기
logo = cv2.imread('data2/opencv-logo-white.png',cv2.IMREAD_UNCHANGED)
src = cv2.imread('data2/cat.bmp')


#모든행,모든열,0~2번채널
logo = img[:,:,:-1]
#알파채널만 슬라이싱
mask = logo[:,:,3]
# print(mask.shape)
#mask의 영역
h,w =mask.shape[:2]
crop =src[10:10+h,10:10+w]

#마스크연산
cv2.copyTo(logo,mask,crop)
cv2.imshow('src',src)
cv2.imshow('mask',mask)
cv2.imshow('img',mask)
#cv2.imshow('img',dst)
cv2.waitKey()
cv2.destroyAllWindows()