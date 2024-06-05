"""
 @author saozd
 @project pytonworkspace MeanBlurSample
 @date 02 Oca 2024
 <p>
 @description:Mean Blur Algoritması Deneme
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

# Mean blur işlemi uygula
blur = cv2.blur(img, (5, 5), (0, 0)) #5x5 boyutunda kutu filtre uygulandı sol üst köşe merkez alındı

# Orijinal resmi ve blur işlemi uygulanmış resmi ekranda göster
cv2.imshow("Orijinal", img)
cv2.imshow("Blur", blur)

# Pencereyi kapatmak için bir tuşa bas
cv2.waitKey(0)
cv2.destroyAllWindows()
