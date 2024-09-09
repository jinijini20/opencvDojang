import cv2
import numpy as np

# 이미지 불러오기
image = cv2.imread('mission/03.png')

# 밝기 감소 비율 (0~1)
brightness_reduction = 0.8

# 이미지 어둡게 만들기
darker_image = cv2.addWeighted(image, brightness_reduction, image, 0, 0)

# Bilateral Filtering 적용 (노이즈 제거, 경계선 유지)
filtered_image = cv2.bilateralFilter(darker_image, 9, 75, 75)

# 이미지 보여주기
cv2.imshow('Enhanced Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

