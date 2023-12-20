"""
 @author saozd
 @project pytonworkspace SurfAlgorithm
 @date 18 Ara 2023
 <p>
 @description: pip install opencv-contrib-python kütüphanesi gerekli
 ORB SURF ile aynı
 https://www.youtube.com/watch?v=fIpTks0G2m0&t=50s
"""
import cv2
import cv2 as cv

# Resimleri oku
image1 = cv2.imread('C:/Users/xsaozdemir/PycharmProjects/pytonworkspace/computervision/article-research/surf-algorithm/original_image.png', cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('C:/Users/xsaozdemir/PycharmProjects/pytonworkspace/computervision/article-research/surf-algorithm/image2.png', cv2.IMREAD_GRAYSCALE)

# SURF detektörünü oluştur
surf = cv2.xfeatures2d.SURF_create()

# Keypoint'leri ve açıklıkları bul
keypoints1, descriptors1 = surf.detectAndCompute(image1, None)
keypoints2, descriptors2 = surf.detectAndCompute(image2, None)

# Brute-Force Matcher kullanarak eşleştirmeleri bul
bf = cv2.BFMatcher()
matches = bf.match(descriptors1, descriptors2)

# Eşleşmeleri mesafe sırasına göre sırala
matches = sorted(matches, key=lambda x: x.distance)

# Eşleşmeleri görselleştir
img_matches = cv2.drawMatches(image1, keypoints1, image2, keypoints2, matches[:10], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

# Görseli ekranda göster
cv2.imshow('SURF Matches', img_matches)
cv2.waitKey(0)
cv2.destroyAllWindows()