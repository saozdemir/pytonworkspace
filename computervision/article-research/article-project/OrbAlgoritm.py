"""
 @author Seyit Ahmet ÖZDEMİR
 @project pytonworkspace OrbAlgoritm
 @date 20 Ara 2023
 <p>
 @description:SURF Algoritmasına benzer yapıya sahip Orb Algoritması örneği
"""
import cv2
import os
import numpy as np

resource_root = r'E:\PycharmProjects\pytonworkspace\computervision\article-research\resources'

# Görüntüleri oku
img1_path = os.path.join(resource_root, 'MGH10/MGH10/g1.png')
img2_path = os.path.join(resource_root, 'MGH10/MGH10/g2.png')

img1 = cv2.imread(img1_path, 0)  # referans görüntü
img2 = cv2.imread(img2_path, 0)  # hareketli görüntü

# ORB özellik çıkarıcıyı başlat
orb = cv2.ORB_create()

# ORB özelliklerini çıkar
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# BFMatcher nesnesi oluştur
bf = cv2.BFMatcher()

# Eşleştirmeleri bul
matches = bf.knnMatch(des1, des2, k=2)

# İyi eşleştirmeleri belirle
good_matches = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good_matches.append(m)

img_wrap=img2
# Eğer yeterli sayıda iyi eşleştirme varsa, görüntüyü kaydır
if len(good_matches) > 10:
    src_pts = np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

    # Doğru eşleşmelerin sayısını kontrol et
    if M is not None and np.sum(mask) > 10:
        h, w = img1.shape
        img_wrap = cv2.warpPerspective(img2, M, (w, h))

img_matches = cv2.drawMatches(img1, kp1, img2, kp2, good_matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

cv2.imshow('Eşleşmeler', img_matches)
cv2.imshow('Kaydırılmış Görüntü', img_wrap)
cv2.waitKey(0)
cv2.destroyAllWindows()