import cv2
import numpy as np
#흰캔버스만들기
img =np.zeros(shape=(512,512,3),dtype=np.uint8) +255
#사각형좌표4개 설정
pts1=np.array([[100,100],[200,100],[200,200],[100,200]])
#위의 좌표4개를 이용해서 그리기
cv2.polylines(img,[pts1],isClosed=True,color =(255,0,0))

pts2=np.array([[300,100],[400,100],[400,200]])
cv2.polylines(img,[pts2],isClosed=True,color =(255,0,0))



cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()