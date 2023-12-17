"""
 @author saozd
 @project pytonworkspace SiftTemplate
 @date 15 Ara 2023
 <p>
 @description:
"""
import cv2
import numpy as np

def sift_feature_matching(img1_path, img2_path):
    # Görüntüleri oku
    img1 = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(img2_path, cv2.IMREAD_GRAYSCALE)

    # SIFT özellik çıkarıcıyı oluştur
    sift = cv2.SIFT_create()

    # Keypoint'leri ve açıklıkları bul
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)

    # Brute-Force Matcher'ı oluştur
    bf = cv2.BFMatcher()

    # İki görüntü arasındaki eşleştirmeleri bul
    matches = bf.knnMatch(des1, des2, k=2)

    # Eşleştirmeleri iyi eşleştirmelerle filtrele
    good_matches = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append(m)

    # Eşleşmeleri görselleştir
    img_matches = cv2.drawMatches(img1, kp1, img2, kp2, good_matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    # Sonucu göster
    cv2.imshow("SIFT Feature Matching", img_matches)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Örnek kullanım
if __name__ == "__main__":

    img1_path = "E:/PycharmProjects/pytonworkspace/computervision/article-research/sift-algorithm/sift-template/resim3.png"
    img2_path = "E:/PycharmProjects/pytonworkspace/computervision/article-research/sift-algorithm/sift-template/resim4.png"
    sift_feature_matching(img1_path, img2_path)
