import cv2
import matplotlib.pyplot as plt
bgr_currentFrame = cv2.imread('image1.png')
xyz_currentFrame = cv2.cvtColor(bgr_currentFrame, cv2.COLOR_BGR2XYZ)
gray_currentFrame = cv2.cvtColor(xyz_currentFrame, cv2.COLOR_BGR2GRAY)
level, otsu_currentFrame = cv2.threshold(gray_currentFrame, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
filtered_currentFrame = cv2.medianBlur(otsu_currentFrame, 5)
num, labels, stats, centroid = cv2.connectedComponentsWithStats(filtered_currentFrame)
print(num-1)
plt.imshow(filtered_currentFrame)
handle = plt.subplot()
for i in range(num):
    if stats[i, cv2.CC_STAT_AREA] <1:
        handle.scatter(centroid[i, 0], centroid[i, 1])
        filtered_currentFrame[labels == i] = 0
num1, labels1, stats1, centroid1 = cv2.connectedComponentsWithStats(filtered_currentFrame)
cv2.imshow('bgr_currentFrame',bgr_currentFrame)
plt.show()
cv2.waitKey(0)

