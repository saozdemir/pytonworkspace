"""
 @author saozd
 @project pytonworkspace Algorithm2
 @date 10 Kas 2023
 <p>
 @description:
"""
from PIL import Image
import pandas as pd

# Resmi yükle
img = Image.open("C:\\Users\\saozd\\Desktop\\Yüksek Lisans\\2023-2024 Güz (1. Sınıf)\\Bilgisayarlı Görü\\kirmizi.png")  # Resminizin dosya yolu ve adını buraya yazın
  # Resminizin dosya yolu ve adını buraya yazın

# Resmi 50x50 boyutuna yeniden ölçeklendir
img = img.resize((50, 50))

# Resmi RGB formatına dönüştür
img = img.convert("RGB")

# Pikselleri al
pixel_values = list(img.getdata())

# Her pikselin R, G, B değerlerini ayrı sütunlarda depolamak için bir liste oluştur
data = []

for pixel in pixel_values:
    data.extend(pixel)

# Veriyi bir DataFrame'e dönüştür
df = pd.DataFrame([data[i:i+3] for i in range(0, len(data), 3)], columns=["R", "G", "B"])

# 50x50 piksel boyutunda bir matrise dönüştür
pixel_matrix = df.values.reshape((50, 50, 3))

# Her bir pikseli bir satır olarak almak isterseniz:
df_unstacked = df.unstack().reset_index(drop=True).to_frame().T

# DataFrame'i Excel'e dök
df_unstacked.to_excel("output.xlsx", index=False, header=False)

