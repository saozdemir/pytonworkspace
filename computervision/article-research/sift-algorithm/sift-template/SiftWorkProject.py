import cv2
import numpy as np

# Görüntüleri oku
img1 = cv2.imread('C:/Users/xsaozdemir/PycharmProjects/pytonworkspace/computervision/article-research/surf-algorithm/original_image.png',0)  # referans görüntü
img2 = cv2.imread('C:/Users/xsaozdemir/PycharmProjects/pytonworkspace/computervision/article-research/surf-algorithm/image2.png',0)  # hareketli görüntü

# SIFT özellik çıkarıcıyı başlat
sift = cv2.SIFT_create()

# SIFT özelliklerini çıkar
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)

# BFMatcher nesnesi oluştur
bf = cv2.BFMatcher()

# Eşleştirmeleri bul
matches = bf.knnMatch(des1,des2,k=2)

# İyi eşleştirmeleri belirle
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append(m)

# Eğer yeterli sayıda iyi eşleştirme varsa, görüntüyü kaydır
if len(good)>10:
    src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
    dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)

    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
    h,w = img1.shape
    img2 = cv2.warpPerspective(img2,M,(w,h))

cv2.imshow('Kaydırılmış Görüntü',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()