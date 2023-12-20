"""
 @author saozd
 @project pytonworkspace DemonsAlgorithm
 @date 20 Ara 2023
 <p>
 @description:
"""
import cv2
import os
import numpy as np

resource_root = r'E:\PycharmProjects\pytonworkspace\computervision\article-research\resources'
# Görüntüleri oku
img1_path = os.path.join(resource_root, '../resources/MGH10/MGH10/g1.png')
img2_path = os.path.join(resource_root, '../resources/MGH10/MGH10/g2.png')

img1 = cv2.imread(img1_path, 0)  # referans görüntü
img2 = cv2.imread(img2_path, 0)  # hareketli görüntü

# Görüntü boyutlarını al
h, w = img1.shape

# Şeytanın enerjisini sıfırla
E_d = 0

# Şeytanın güç vektörlerini tutacak bir matris oluştur
F = np.zeros((h, w, 2), dtype=np.float32)  # Veri tipini CV_32F olarak belirt

# Şeytanın güç vektörlerini düzeltmek için bir Gauss çekirdeği oluştur
sigma = 1  # Çekirdeğin standart sapması
ksize = 3  # Çekirdeğin boyutu
kernel = cv2.getGaussianKernel(ksize, sigma)
kernel = np.outer(kernel, kernel)

# İterasyon sayısını belirle
n_iter = 10

img_wrap=img2
# Her iterasyonda
for i in range(n_iter):
    # Görüntüleri yeniden kaydır
    img_wrap = cv2.remap(img2, F[:, :, 0].astype(np.float32), F[:, :, 1].astype(np.float32), cv2.INTER_LINEAR)

    # Görüntüler arasındaki farkı hesapla
    diff = img1 - img_wrap

    # Görüntüler arasındaki gradyanı hesapla
    grad_x = cv2.Sobel(img_wrap, cv2.CV_64F, 1, 0, ksize=5)
    grad_y = cv2.Sobel(img_wrap, cv2.CV_64F, 0, 1, ksize=5)
    grad = np.sqrt(grad_x ** 2 + grad_y ** 2)

    # Görüntüler arasındaki benzerliği hesapla
    sim = diff / (grad + 1e-5)

    # Şeytanın güç vektörlerini güncelle
    F[:, :, 0] += sim * grad_x
    F[:, :, 1] += sim * grad_y

    # Şeytanın güç vektörlerini düzelt
    F[:, :, 0] = cv2.filter2D(F[:, :, 0], -1, kernel)
    F[:, :, 1] = cv2.filter2D(F[:, :, 1], -1, kernel)

# Eşleşmeleri görselleştir
img_matches = cv2.drawMatches(img1, None, img2, None, None, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

cv2.imshow('Eşleşmeler', img_matches)
cv2.imshow('Kaydırılmış Görüntü', img_wrap)
cv2.waitKey(0)
cv2.destroyAllWindows()
