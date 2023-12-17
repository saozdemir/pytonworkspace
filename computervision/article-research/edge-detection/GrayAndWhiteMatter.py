"""
 @author saozd
 @project pytonworkspace GrayAndWhiteMatter
 @date 17 Ara 2023
 <p>
 @description:
"""
import cv2
import numpy as np

# Beyin CT görüntüsünü yükle
img = cv2.imread('E:/PycharmProjects/pytonworkspace/computervision/article-research/edge-detection/image2.png', cv2.IMREAD_GRAYSCALE)

# Beyin CT görüntüsünü normalize et
normalized_img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)

# Beyin CT görüntüsünü eşikle (beyin dokularını belirlemek için)
_, thresholded_img = cv2.threshold(normalized_img, 30, 255, cv2.THRESH_BINARY)

# Gri madde haritası
gray_matter_map = cv2.bitwise_and(normalized_img, normalized_img, mask=thresholded_img)

# Beyaz madde haritası (tüm beyin haritasından gri madde haritasını çıkar)
white_matter_map = cv2.subtract(normalized_img, gray_matter_map)

# Sonuçları görselleştir
cv2.imshow('Original CT Image', normalized_img)
cv2.imshow('Gray Matter Map', gray_matter_map)
cv2.imshow('White Matter Map', white_matter_map)
cv2.waitKey(0)
cv2.destroyAllWindows()