"""
 @author saozd
 @project pytonworkspace OtsuAlgorithm
 @date 18 Ara 2023
 <p>
 @description:
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Görüntüyü yükle
image = cv2.imread('E:/PycharmProjects/pytonworkspace/computervision/otsu-algorithm/1024x576.png', 0)  # Gri tonlamalı olarak yükle

# Otsu thresholding uygula
_, otsu_thresholded = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Orijinal ve Otsu Tresholding sonuçlarını göster
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Orijinal Görüntü')
plt.imshow(image, cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Otsu Tresholding')
plt.imshow(otsu_thresholded, cmap='gray')

plt.show()