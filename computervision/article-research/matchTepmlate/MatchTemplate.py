"""
 @author saozd
 @project pytonworkspace MatchTemplate
 @date 18 Ara 2023
 <p>
 @description:
"""
import cv2

# Resimleri oku
image1 = cv2.imread('E:/PycharmProjects/pytonworkspace/computervision/article-research/edge-detection/original_image.png')
image2 = cv2.imread('E:/PycharmProjects/pytonworkspace/computervision/article-research/edge-detection/image2.png')

# Gri tonlamaya çevir
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# Normalized Cross-Correlation (NCC) ile benzerlik ölçümü
result_ncc = cv2.matchTemplate(gray1, gray2, cv2.TM_CCORR_NORMED)

# Sum of Squared Differences (SSD) ile benzerlik ölçümü
result_ssd = cv2.matchTemplate(gray1, gray2, cv2.TM_SQDIFF)

# Benzerlik haritasını görselleştir
cv2.imshow('NCC Result', result_ncc)
cv2.imshow('SSD Result', result_ssd)

# Bekle ve pencereyi kapat
cv2.waitKey(0)
cv2.destroyAllWindows()