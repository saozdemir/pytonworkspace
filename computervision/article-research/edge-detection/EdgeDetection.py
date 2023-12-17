"""
 @author saozd
 @project pytonworkspace EdgeDetection
 @date 17 Ara 2023
 <p>
 @description:
"""
import cv2
import numpy as np

def edge_detection(image_path):
    # Resmi oku
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Giriş resmi 3 kanala sahip mi?
    if len(image.shape) == 3 and image.shape[2] == 3:
        # Gri tonlamaya dönüştür
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        # Resim zaten gri tonlama
        gray = image

    # Gri tonlama görüntüsünü threshold ile siyah-beyaz'a çevir
    _, binary_image = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)#128

    # Kenar tespiti yap
    edges = cv2.Canny(binary_image, 50, 150)

    # Sonuçları göster
    cv2.imshow('Original Image', image)
    cv2.imshow('Gray Image', gray)
    cv2.imshow('Binary Image', binary_image)
    cv2.imshow('Edge Detection', edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Örnek kullanım
if __name__ == "__main__":
    image_path = "E:/PycharmProjects/pytonworkspace/computervision/article-research/edge-detection/image2.png"
    edge_detection(image_path)