"""
 @author Seyit Ahmet ÖZDEMİR
 @project pytonworkspace EdgeDetection
 @date 20 Ara 2023
 <p>
 @description: Sınır Tespit Algoritması uygulasması
"""
import cv2
import os

# Resource root tanımlama
resource_root = r'E:\PycharmProjects\pytonworkspace\computervision\article-research\resources'

# Görüntüleri oku
img_path = os.path.join(resource_root, 'MGH10/MGH10/g2.png')

# Resmi Gray Scale'a dönüştür
image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

# Eşikleme işlemi ile gri madde ve beyaz madde ayrımı yap (eşik değeri tanımlama)
_, thresholded_gray_matter = cv2.threshold(image, 50, 255, cv2.THRESH_BINARY)  # 30
_, thresholded_white_matter = cv2.threshold(image, 70, 255, cv2.THRESH_BINARY_INV)

# gri madde kenarları
gray_edges = cv2.Canny(thresholded_gray_matter, 50, 150)
# beyaz madde kenarları
white_edges = cv2.Canny(thresholded_white_matter, 50, 150)

# Gri madde ve beyaz maddeyi birleştir
combined_image = cv2.bitwise_and(thresholded_gray_matter, thresholded_white_matter)

# yeni gri kenarlıklar
gray_edges_new = cv2.Canny(combined_image, 50, 150)


# combined_edges = cv2.bitwise_and(gray_edges, white_edges)
combined_edges = cv2.bitwise_and(gray_edges_new, white_edges)

# Kenar tespiti yap
edges = cv2.Canny(combined_image, 50, 150)

# Sonuçları göster
cv2.imshow('Original Image', image)
cv2.imshow('Gray Matter', combined_image)
cv2.imshow('White Matter', 255 - thresholded_white_matter)
# cv2.imshow('Combined Image', combined_image)
cv2.imshow('Edge Detection', edges)
cv2.imshow('Gray Edge Detection', gray_edges_new-white_edges)
cv2.imshow('White Edge Detection', white_edges)
# cv2.imshow('Combine Edge Detection', combined_edges)

cv2.waitKey(0)
cv2.destroyAllWindows()