import cv2
import numpy as np

image = cv2.imread('picture_10_01.jpg')

z = image.shape[0]
zx = image.shape[1]

for i in range(z):
    for j in range(zx):
        min = np.argmin(image[i, j])
        image[i, j, min] = 0

cv2.imwrite('picture_10_01_1.jpg', image)