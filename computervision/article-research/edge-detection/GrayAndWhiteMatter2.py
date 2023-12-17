"""
 @author saozd
 @project pytonworkspace GrayAndWhiteMatter2
 @date 18 Ara 2023
 <p>
 @description:
"""
import matplotlib.pyplot as plt
import cv2
import numpy as np

# Beyin görüntüsü yükleyin
brain_image = plt.imread("E:/PycharmProjects/pytonworkspace/computervision/article-research/edge-detection/image2.png")

# Gri tonlamalı görüntüyü oluşturun
gray_matter = brain_image[:, :, 0]
white_matter = brain_image[:, :, 1]

# Gri madde ve beyaz madde haritalarını gösterin
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.imshow(gray_matter, cmap="gray")
ax1.set_title("Gri Madde Haritası")
ax2.imshow(white_matter, cmap="gray")
ax2.set_title("Beyaz Madde Haritası")
plt.show()

cv2.imshow("Gri Madde Haritası", gray_matter)
cv2.imshow("Beyaz Madde Haritası", white_matter)
cv2.waitKey(0)
cv2.destroyAllWindows()