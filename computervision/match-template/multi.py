"""
 @author saozd
 @project pytonworkspace multi
 @date 19 Kas 2023
 <p>
 @description:
"""
import cv2
import numpy as np

# Görüntüyü ve şablonu yükle
imgOrj= cv2.imread('buyuk_goruntu.png')
imgTepmlate = template = cv2.imread('sablon.png')
img = cv2.cvtColor(imgOrj, cv2.COLOR_BGR2GRAY)
template = cv2.cvtColor(imgTepmlate, cv2.COLOR_BGR2GRAY)

# Korelasyon matrisi
I_normalized = (img - np.mean(img)) / np.std(img)
T_normalized = (template - np.mean(template)) / np.std(template)

# Korelasyon hesaplama
correlation_matrix = np.correlate(I_normalized.flatten(), T_normalized.flatten(), mode='full')

# Korelasyon matrisini yeniden boyutlandırma
correlation_matrix = np.resize(correlation_matrix, (img.shape[0] - template.shape[0] + 1, img.shape[1] - template.shape[1] + 1))


# Şablonun boyutlarını al
h, w = template.shape[:2]

# Eşleştirme yöntemini seç (örneğin, cv2.TM_CCOEFF_NORMED kullanılabilir)
method = cv2.TM_CCOEFF_NORMED  #korelasyon katsayısını normal şekilde kullanır

# Eşleştirmeyi gerçekleştir
result = cv2.matchTemplate(img, template, method)

# Belirli bir eşik değeri üzerindeki eşleşmeleri bul
threshold = 0.8
loc = np.where(result >= threshold)

# Tüm eşleşmeleri işaretle
for pt in zip(*loc[::-1]):
    top_left = pt
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 1)


# Eşik değerini geçen piksellerin konumlarını bulma
matching_points = np.where(correlation_matrix >= threshold)

print("\nKorelasyon Matrisi:")
print(correlation_matrix)

# Sonuçları gösterme
print("Eşik değerini geçen piksellerin konumları:")
for pt in zip(*matching_points):
    print("Şablonun konumu:", pt)


# Sonucu göster
cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()