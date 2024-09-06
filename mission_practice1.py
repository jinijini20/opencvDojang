import cv2
import numpy as np

# 이미지 읽기
img = cv2.imread('mission/01.png')

# HSV 색공간으로 변환
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 얼룩의 HSV 값 범위 설정 (예시)
lower_blue = np.array([100, 43, 46])
upper_blue = np.array([124, 255, 255])

# 마스크 생성
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# 원본 이미지에서 마스크 영역 제거
result = cv2.bitwise_and(img, img, mask=~mask)

# 결과 이미지 출력
cv2.imshow('Original', img)
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()