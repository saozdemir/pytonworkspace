"""
 @author saozd
 @project pytonworkspace MedyanBlurSample
 @date 02 Oca 2024
 <p>
 @description:Medyan Blur Algoritması
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
blur = cv2.medianBlur(img, 7) #Kernel boyutu tek tam sayı olmalıdır.
# Kernel boyutu ne kadar büyük olursa o kadar bulanık olur.
# Medyan değeri bir veri kümesinin ortasında kalan değerdir. [1,2,3,4,5] de değer 3 olur.

# Orijinal resmi ve blur işlemi uygulanmış resmi ekranda göster
cv2.imshow("Orijinal", img)
cv2.imshow("Blur", blur)

# Pencereyi kapatmak için bir tuşa bas
cv2.waitKey(0)
cv2.destroyAllWindows()