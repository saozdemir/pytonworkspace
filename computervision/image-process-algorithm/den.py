import cv2

# Resmi oku
image = cv2.imread("C:/Users/xsaozdemir/PycharmProjects/pytonworkspace/computervision/image-process-algorithm/50x50.png")

# Gri tonlamalıya çevir
# Orijinal resmin gri tonlamalıya çevrilmesi
gray_original = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Orijinal resmin gri tonlamalı değerlerini yazdır
print("Orijinal Resmin Gri Tonlamalı Değerleri:")
for i in range(gray_original.shape[0]):
    for j in range(gray_original.shape[1]):
        print(f"Pixel({i},{j}): {gray_original[i, j]}")

# INTER_NEAREST algoritması ile resmi 20x20 boyutuna küçült
resized = cv2.resize(image, (20, 20), interpolation=cv2.INTER_NEAREST)

# Küçültülmüş resmin gri tonlamalıya çevrilmesi
gray_resized = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

# Küçültülmüş resmin gri tonlamalı değerlerini yazdır
print("\nKüçültülmüş Resmin Gri Tonlamalı Değerleri:")
for i in range(gray_resized.shape[0]):
    for j in range(gray_resized.shape[1]):
        print(f"Pixel({i},{j}): {gray_resized[i, j]}")
        #ROUND FONKSİYONU KULLANNNN!!!!