import cv2
import os
from PIL import Image
import numpy as np

# scale factor는 1에 가까울수록 인식율이 좋지만 그만큼 느려짐
SF  = 1.02
# 내부 알고리즘에서 최소한 검출된 횟수이상 되야 인식
N = 2
# 검출하려는 이미지의 최소 사이즈
MS=(100,100)

# 고양이 얼굴 인식용 haarcascade 파일 위치 
cascade = '../opencv/opencv/data/haarcascades/haarcascade_frontalcatface.xml'

# 고양이 얼굴 인식 cascade 생성 
face_cascade = cv2.CascadeClassifier(cascade)

# 얼굴 검출 함수 
def detectCatFace(imgPath):
    result = False
    # 이미지 불러오기 
    ff = np.fromfile(imgPath, np.uint8)
    img = cv2.imdecode(ff, cv2.IMREAD_COLOR)
    # 회색으로 변경 
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 얼굴 검출
    faces = face_cascade.detectMultiScale(grayImg, scaleFactor=SF, minNeighbors=N, minSize=MS)
    # 얼굴 검출 1개인 경우만 승인
    if len(faces) == 1:
        result = True
    else:
        result = False
    # 출력값
    return result