import cv2,sys
import numpy as np
from glob import glob
import os

def getImageList():
    basePath =os.getcwd()
    datapath = os.path.join(basePath,'images')
    fileNames = glob(os.path.join(datapath,'*.jpg'))
    
    return fileNames
#corners:좌표(startpt,endpt)
#2개 좌표를 이용해서 직사각형 그리기
def drawROI(img,corners):
    cpy = img.copy()
    line_c =(128,128,255)
    linewidth =2
    
    for corners in boxList:
        cv2.rectangle(cpy,tuple(corners[0]),tuple(corners[0]),color=line_c,thickness=linewidth)
    