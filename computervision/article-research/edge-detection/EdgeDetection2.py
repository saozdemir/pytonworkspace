"""
 @author saozd
 @project pytonworkspace EdgeDetection2
 @date 17 Ara 2023
 <p>
 @description:
"""
import cv2
import numpy as np

def process_brain_mri(image_path):
    # Resmi oku
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Eşikleme işlemi ile gri madde ve beyaz madde ayrımı yap
    _, thresholded_gray_matter = cv2.threshold(image, 50, 255, cv2.THRESH_BINARY)#30
    _, thresholded_white_matter = cv2.threshold(image, 70, 255, cv2.THRESH_BINARY_INV)

    #gri madde kenarları
    gray_edges = cv2.Canny(thresholded_gray_matter, 50, 150)
    #beyaz madde kenarları
    white_edges = cv2.Canny(thresholded_white_matter, 50, 150)

    # Gri madde ve beyaz maddeyi birleştir
    combined_image = cv2.bitwise_and(thresholded_gray_matter, thresholded_white_matter)
    combined_edges = cv2.bitwise_and(gray_edges, white_edges)

    # Kenar tespiti yap
    edges = cv2.Canny(combined_image, 50, 150)

    # Sonuçları göster
    cv2.imshow('Original Image', image)
    cv2.imshow('Gray Matter', thresholded_gray_matter)
    cv2.imshow('White Matter', 255-thresholded_white_matter)
    cv2.imshow('Combined Image', combined_image)
    cv2.imshow('Edge Detection', edges)
    cv2.imshow('Gray Edge Detection', gray_edges)
    cv2.imshow('White Edge Detection', white_edges)
    cv2.imshow('Combine Edge Detection', combined_edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Örnek kullanım
if __name__ == "__main__":
    brain_mri_path = "E:/PycharmProjects/pytonworkspace/computervision/article-research/edge-detection/original_image.png"
    process_brain_mri(brain_mri_path)