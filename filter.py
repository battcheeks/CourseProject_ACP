import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('example_01.png')
kernel = np.ones((5,5),np.float32)/25
dst = cv.filter2D(img,-1,kernel)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()
blur = cv.GaussianBlur(img,(5,5),0)
median = cv.medianBlur(img,5)
blur1 = cv.bilateralFilter(img,9,75,75)
cv.imshow('Gaussian Blur',blur)
cv.imshow('Median Blur',median)
cv.imshow('Bilateral Blur',blur1)
cv.waitKey()
cv.destroyAllWindows()