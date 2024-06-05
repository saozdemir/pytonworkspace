"""
 @author saozd
 @project pytonworkspace Blurrr
 @date 04 Oca 2024
 <p>
 @description:
"""
import os

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Görüntüyü oku
resource_root = r'E:\PycharmProjects\pytonworkspace\computervision\blur\resources'

# Görüntüleri oku
img1_path = os.path.join(resource_root, 'sample_image.PNG')
# Bir resmi oku
img = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE)

# Mean filtre uygula
mean_blur = cv2.blur(img, (5, 5))

# Medyan filtre uygula
median_blur = cv2.medianBlur(img, 5)

# Gaussian Blur uygula
gaussian_blur = cv2.GaussianBlur(img, (5, 5), 0)

# Histogram analizi için fonksiyon
def plot_histogram(image, title):
    histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
    plt.plot(histogram, color='black')
    plt.title(title)
    plt.xlabel('Pixel Değerleri')
    plt.ylabel('Frekans')
    plt.show()

# Orijinal görüntü histogram analizi
plot_histogram(img, "Orijinal Görüntü Histogramı")

# Mean Blur sonrası histogram analizi
plot_histogram(mean_blur, "Mean Blur Sonrası Histogram")

# Medyan Blur sonrası histogram analizi
plot_histogram(median_blur, "Medyan Blur Sonrası Histogram")

# Gaussian Blur sonrası histogram analizi
plot_histogram(gaussian_blur, "Gaussian Blur Sonrası Histogram")

# Görüntüleri göster
cv2.imshow("Orijinal Görüntü", img)
cv2.imshow("Mean Blur", mean_blur)
cv2.imshow("Medyan Blur", median_blur)
cv2.imshow("Gaussian Blur", gaussian_blur)

# Pencereyi kapatmak için bir tuşa bas
cv2.waitKey(0)
cv2.destroyAllWindows()
