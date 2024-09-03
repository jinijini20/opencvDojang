import cv2,sys

#videoCapture() 클래스 객체 생성

cap=cv2.VideoCapture(0)


print(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),\
      int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

cap.set(cap.get(cv2.CAP_PROP_FRAME_WIDTH,640))
cap.set(cap.get(cv2.CAP_))