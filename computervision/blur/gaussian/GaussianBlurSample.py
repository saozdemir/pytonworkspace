"""
 @author saozd
 @project pytonworkspace GaussianBlurSample
 @date 02 Oca 2024
 <p>
 @description:Gaussian Blur Algoritması Örneği
"""
# OpenCV ve numpy kütüphanelerini içe aktar
import cv2
import os
import numpy as np


resource_root = r'E:\PycharmProjects\pytonworkspace\computervision\blur\resources'

# Görüntüleri oku
img1_path = os.path.join(resource_root, 'sample_image.PNG')
# Bir resmi oku
img = cv2.imread(img1_path)

# Medyan blur işlemi uygula
blur = cv2.GaussianBlur(img, (5, 5), 1, 0,1)
# (5,5) gaussian filtre boyutu
# sigmax ve sigmay standart fağma değerleri
# dst çıktı resminin depolanacağı NumPy dizisi

# Orijinal resmi ve blur işlemi uygulanmış resmi ekranda göster
cv2.imshow("Orijinal", img)
cv2.imshow("Blur", blur)

# Pencereyi kapatmak için bir tuşa bas
cv2.waitKey(0)
cv2.destroyAllWindows()