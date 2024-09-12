#1.배경: 흰색 책상, 우드 테이블
#2. 데이터 증식 조건
#  2-0 스마트폰으로 사진 촬영 후 이미지 크기를 줄여주자. (이미지 크기 224x224)
#      대상물 촬영을 어떻게 해야할지 확인 
#  2-1 rotate: 회전(10~30도) 범위 안에서 어느 정도 각도를 넣어야 인식이 잘되는가?
#  2-2 hflip,vflip : 도움이 되는가?,넣을 것인가?
#  2-3 resize,crop :가능하면 적용해 보자
#  2-4 파일명을 다르게 저장 cf) jelly_wood.jpg,jelly_white.jpg
   # jelly_wood_rot_15.jpg ,jelly_wood_hflip.jpg,jelly_wood_resize.jpg
#  2-5 클래스 별로 폴더를 생성
#  2-6 데이터를 어떻게 넣느냐에 따라 어떻게 동작되는지 1-2줄로 요약

# 구성 순서
# 1.촬영한다
#2.이미지를 컴퓨터로 복사,resize한다
#3.육안으로 확인, 이렇게 사용해도 되는가?
#4.함수들을 만든다. rotate,crop,hflip,vflip 
# 원본파일명을 읽어서 파일명을 생성하는 기능은 모든 함수에 있어야 한다.(함수)
# 5.단일 함수를 검증
# 함수를 활용해서 기능 구현
#테스트(경우의수)
#8.데이터셋을 techable machine사이트에 올려서 테스트
#9. 인식이 잘 안되는 케이스를 분석하고 케이스 추가 1-8에서 구현된 기능을 이용

# dataPath = os.path(os.getcwd(),'DataAug')
# dataOrg = os.path.join(dataPath,'org')
# fileName = os.path.join(dataOrg,'carkey_white.jpg')
# # print(fileName)
# img = cv2.imread(fileName)
# img_resize = cv2.resize(img,(224,224))
# cv2.imshow('resize',img_resize)
# cv2.waitKey()
# cv2.destroyAllWindows()

import cv2,sys
import numpy as np
import os

impath = os.path.join(os.getcwd(),'dataArg')
dataOrg = os.path.join(impath,'ex_1')
filename= os.path.join(dataOrg,'silver_white.jpg')
# print(filename)
img = cv2.imread(filename)

img_resize =cv2.resize(img,(224,224))
img90 = cv2.rotate(img_resize,cv2.ROTATE_90_CLOCKWISE)
img180 = cv2.rotate(img_resize,cv2.ROTATE_180)


def rotate_image(image, angle):
    # 이미지의 크기 (height, width) 구하기
    (h, w) = image.shape[:2]
    
    # 회전의 중심점 설정 (보통 이미지의 가운데)
    center = (w // 2, h // 2)
    
    # 회전 변환 행렬 생성
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    
    # 이미지 회전
    rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))
    
    return rotated_image
 
 
 
 
 
 
 # 이미지 불러오기
img = cv2.imread(img_resize)

# 이미지 회전 (45도)
rotated_img = rotate_image(img, 45)

# # 회전된 이미지 저장
# cv2.imwrite('rotated_image.jpg', rotated_img)



cv2.imshow('rotated_img',rotated_img)
cv2.waitKey()
cv2.destroyAllWindows()





# cv2.imshow('resize',img_resize)
# cv2.waitKey()
# cv2.destroyAllWindows()

