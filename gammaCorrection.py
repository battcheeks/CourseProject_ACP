
from builtins import input
import cv2 as cv
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Code for Changing the contrast and brightness of an image! tutorial.')
parser.add_argument('--input', help='Path to input image.', default='xray.jpg')
args = parser.parse_args()
image = cv.imread(cv.samples.findFile(args.input))
new_image = np.zeros(image.shape, image.dtype)
alpha = 1.5
beta = 20
print(' Basic Linear Transforms ')
print('-------------------------')
print('For preset values of alpha and beta which are: ',alpha ,beta)

for y in range(image.shape[0]):
    for x in range(image.shape[1]):
        for c in range(image.shape[2]):
            new_image[y,x,c] = np.clip(alpha*image[y,x,c] + beta, 0, 255)
cv.imshow('Original Image', image)
cv.imshow('New Image', new_image)

cv.waitKey(0)
cv.destroyAllWindows()