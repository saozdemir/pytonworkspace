"""
 @author saozd
 @project pytonworkspace ShiftComparison
 @date 17 Ara 2023
 <p>
 @description:
"""
import cv2
import numpy as np

# Görüntüyü yükle
img = cv2.imread('E:/PycharmProjects/pytonworkspace/computervision/article-research/sift-algorithm/shift-comparison/brain.PNG')

# Kaydırma miktarını belirle (x, y)
shift_amount = (50, 30)

# Kaydırma matrisini oluştur
shift_matrix = np.float32([[1, 0, shift_amount[0]], [0, 1, shift_amount[1]]])

# Görüntüyü kaydır
shifted_img = cv2.warpAffine(img, shift_matrix, (img.shape[1], img.shape[0]))

# Görüntüyü görselleştir
cv2.imshow('Original Image', img)
cv2.imshow('Shifted Image', shifted_img)
cv2.waitKey(0)
cv2.destroyAllWindows()