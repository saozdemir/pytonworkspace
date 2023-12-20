import cv2
import numpy as np

img1 = cv2.imread('C:/Users/xsaozdemir/PycharmProjects/pytonworkspace/computervision/article-research/surf-algorithm/original_image.png', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('C:/Users/xsaozdemir/PycharmProjects/pytonworkspace/computervision/article-research/surf-algorithm/image2.png', cv2.IMREAD_GRAYSCALE)

orb = cv2.ORB_create()

# Keypoint'leri ve açıklıkları bul
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# Brute-Force Matcher'ı oluştur
bf = cv2.BFMatcher()

# İki görüntü arasındaki eşleştirmeleri bul
matches = bf.knnMatch(des1, des2, k=2)

# RANSAC ile yanlış eşleştirmeleri ele
good_matches = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good_matches.append(m)

src_pts = np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
dst_pts = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

# RANSAC ile dönüşüm matrisini hesapla
_, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

# İyi eşleşmeleri seç
good_matches = [good_matches[i] for i in range(len(good_matches)) if mask[i] == 1]

# Eşleşmeleri görselleştir
img_matches = cv2.drawMatches(img1, kp1, img2, kp2, good_matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

# Eşleştirme sonuçlarını göster
cv2.imshow('ORB Matches with RANSAC', img_matches)
cv2.waitKey(0)
cv2.destroyAllWindows()