import cv2

# 이미지 불러오기
image = cv2.imread('mission/05.png')

# 밝기 감소 비율 (0~1)
brightness_reduction = 0.7

# 이미지 어둡게 만들기
darker_image = cv2.addWeighted(image, brightness_reduction, image, 0, 0)

# 이미지 보여주기
cv2.imshow('Darker Image', darker_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

