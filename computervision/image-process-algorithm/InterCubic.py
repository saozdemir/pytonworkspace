"""
 @author saozd
 @project pytonworkspace InterLCubic
 @date 19 Kas 2023
 <p>
 @description:
"""
import cv2
import pandas as pd

# Resmi oku
image = cv2.imread("C:/Users/saozd/Desktop/50x50.png")

# Gri tonlamalıya çevir
gray_original = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Orijinal resmin gri tonlamalı değerlerini yazdır
print("Orijinal Resmin Gri Tonlamalı Değerleri:")
for i in range(gray_original.shape[0]):
    for j in range(gray_original.shape[1]):
        print(f"Pixel({i},{j}): {gray_original[i, j]}")

# INTER_AREA algoritması ile resmi 20x20 boyutuna küçült
resized = cv2.resize(image, (20, 20), interpolation=cv2.INTER_CUBIC)

# Küçültülmüş resmin gri tonlamalıya çevrilmesi
gray_resized = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

# Küçültülmüş resmin gri tonlamalı değerlerini yazdır
print("\nKüçültülmüş Resmin Gri Tonlamalı Değerleri:")
for i in range(gray_resized.shape[0]):
    for j in range(gray_resized.shape[1]):
        print(f"Pixel({i},{j}): {gray_resized[i, j]}")

# Verileri depolamak için DataFrame oluştur
df_original = pd.DataFrame(gray_original)

# Excel'e yazdır
df_original.to_excel("original_50x50.xlsx", index=False)

# Verileri depolamak için DataFrame oluştur
df_resized = pd.DataFrame(gray_resized)

# Excel'e yazdır
df_resized.to_excel("resized_20x20_inter_cubic.xlsx", index=False)