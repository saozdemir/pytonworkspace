"""
 @author saozd
 @project pytonworkspace OrbAlgortihm
 @date 20 Ara 2023
 <p>
 @description:SURF algoritmasına eşdeğer olarak kullanılabilen ORB algoritması örneği
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
good = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good.append(m)

# Eğer yeterli sayıda iyi eşleştirme varsa, görüntüyü kaydır
if len(good) > 10:
    src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
    h, w = img1.shape
    img2 = cv2.warpPerspective(img2, M, (w, h))

cv2.imshow('Kaydırılmış Görüntü', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
