"""
 @author saozd
 @project pytonworkspace Algorithm4
 @date 10 Kas 2023
 <p>
 @description:
"""
from PIL import Image
import pandas as pd
import os

# Resmi yükle
img = Image.open("C:\\Users\\saozd\\Desktop\\Yüksek Lisans\\2023-2024 Güz (1. Sınıf)\\Bilgisayarlı Görü\\kirmizi.png")  # Resminizin dosya yolu ve adını buraya yazın


# Resmi 50x50 boyutuna yeniden ölçeklendir
img = img.resize((50, 50))

# Resmi RGB formatına dönüştür
img = img.convert("RGB")

# Pikselleri al
pixel_values = list(img.getdata())

# Matrisi oluştur
matrix = []

for i in range(50):
    row = []
    for j in range(50):
        pixel = pixel_values[i * 50 + j]
        row.append(pixel)
    matrix.append(row)

# Veriyi bir DataFrame'e dönüştür
df = pd.DataFrame(matrix, columns=[f'Pixel_{i}' for i in range(50)])
df.index = [f'Pixel_{i}' for i in range(50)]

if os.path.exists("output.xlsx"):
    os.remove("output.xlsx")

# DataFrame'i Excel'e dök
df.to_excel("output.xlsx", index=False)