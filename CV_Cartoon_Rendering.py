import numpy as np
import cv2 as cv

# 이미지 불러오기
img = cv.imread('C:\\Users\\USER\\Desktop\\image1.JPG')

# 흑백 이미지로 변환
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
# 이미지에 bilateralFilter 적용
blr = cv.bilateralFilter(gray, 9, 15, 15)

# 이미지에 Canny Edge 적용
edge = cv.Canny(blr, 60, 140, apertureSize=3)

# Canny Edge 반전 -> 흰 배경에 검은 선
edge = cv.bitwise_not(edge)

# 흑백 이미지를 다시 컬러로 변환
edge = cv.cvtColor(edge, cv.COLOR_GRAY2BGR)

# 원본 이미지와 효과를 준 이미지를 섞어준다
cartoon = cv.bitwise_and(img, edge)

# 이미지 보여주기
cv.imshow('CV_Cartoon_Rendering', cartoon)
cv.waitKey(0)
cv.destroyAllWindows()
