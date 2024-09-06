import cv2,sys
import numpy as np
import matplotlib.pyplot as plt

    


def normalize_image(image, mean=None, std=None):
  """
  OpenCV를 사용하여 이미지를 0과 1 사이의 값으로 정규화합니다.

  Args:
      image: 정규화할 이미지 배열입니다.
      mean: 이미지의 평균 값입니다. 기본값은 None입니다.
      std: 이미지의 표준 편차입니다. 기본값은 None입니다.

  Returns:
      정규화된 이미지 배열입니다.
  """

  # 평균과 표준 편차 계산
  if mean is None:
    mean = np.mean(image)
  if std is None:
    std = np.std(image)

  # 이미지 정규화
  normalized_image = (image - mean) / std

  return normalized_image

# 이미지 로드
image = cv2.imread("mission/01.png")

# 이미지 정규화
normalized_image = normalize_image(image)

# 픽셀화 효과 적용
pixelated_image = cv2.resize(normalized_image, None, fx=0.1, fy=0.1, interpolation=cv2.INTER_NEAREST)
pixelated_image = cv2.resize(pixelated_image, (image.shape[1], image.shape[0]), interpolation=cv2.INTER_NEAREST)

# 이미지 출력
cv2.imshow("Pixelated Image", pixelated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
