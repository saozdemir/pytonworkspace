"""
 @author saozd
 @project pytonworkspace sample
 @date 19 Kas 2023
 <p>
 @description:
"""
import cv2
import numpy as np

# Görüntüyü ve şablonu yükle
imgOrj= cv2.imread('C:/Users/saozd/Desktop/buyuk_goruntu.png')
imgTepmlate = template = cv2.imread('C:/Users/saozd/Desktop/sablon.png')
img = cv2.cvtColor(imgOrj, cv2.COLOR_BGR2GRAY)
template = cv2.cvtColor(imgTepmlate, cv2.COLOR_BGR2GRAY)


# Şablonun boyutlarını al
h, w = template.shape[:2]

# Eşleştirme yöntemini seç (örneğin, cv2.TM_CCOEFF_NORMED kullanılabilir)
method = cv2.TM_CCOEFF_NORMED

# Eşleştirmeyi gerçekleştir
result = cv2.matchTemplate(img, template, method)

# En iyi eşleşmenin konumunu bul
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# Eğer method cv2.TM_CCOEFF_NORMED kullanılıyorsa, en iyi eşleşme max_loc'da olacaktır.
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

# Bulunan bölgeyi dikdörtgenle işaretle
cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)

# Sonucu göster
cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()