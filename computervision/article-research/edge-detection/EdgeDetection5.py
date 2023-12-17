"""
 @author saozd
 @project pytonworkspace EdgeDetection5
 @date 18 Ara 2023
 <p>
 @description:
"""
import cv2
import numpy as np

# Beyin görüntüsü yükleyin
brain_image = cv2.imread("E:/PycharmProjects/pytonworkspace/computervision/article-research/edge-detection/image2.png")

# Gri tonlamalı görüntüyü oluşturun
gray_image = cv2.cvtColor(brain_image, cv2.COLOR_BGR2GRAY)

# Basit bir eşikleme işlemi ile beyaz ve gri maddeyi ayırın
_, thresholded_image = cv2.threshold(gray_image, 20, 255, cv2.THRESH_BINARY)

# Gri madde ve beyaz maddeyi ayırın
gray_matter = cv2.bitwise_and(gray_image, thresholded_image)
white_matter = cv2.bitwise_and(gray_image, cv2.bitwise_not(thresholded_image))

# Kenarlık görüntüsünü çıkarın
edge_image = cv2.Canny(gray_image, 100, 200)

# Gri madde, beyaz madde ve kenarlık görüntülerini gösterin
cv2.imshow("Gri Madde", gray_matter)
cv2.imshow("Beyaz Madde", white_matter)
cv2.imshow("Kenarlık Görüntüsü", edge_image)
cv2.waitKey(0)
cv2.destroyAllWindows()