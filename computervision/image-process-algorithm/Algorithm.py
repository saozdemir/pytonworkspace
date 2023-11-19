"""
 @author saozd
 @project pytonworkspace Algorithm
 @date 10 Kas 2023
 <p>
 @description:
"""
from PIL import Image
import pandas as pd

# Resmi yükle
img = Image.open("C:\\Users\\saozd\\Desktop\\Yüksek Lisans\\2023-2024 Güz (1. Sınıf)\\Bilgisayarlı Görü\\kirmizi.png")  # Resminizin dosya yolu ve adını buraya yazın

# Resmi 50x50 boyutuna yeniden ölçeklendir
img = img.resize((50, 50))

# Resmi RGB formatına dönüştür
img = img.convert("RGB")

# Pikselleri al
pixel_values = list(img.getdata())

# Her pikselin R, G, B değerlerini ayrı sütunlarda depolamak için bir liste oluştur
data = []

for pixel in pixel_values:
    data.append(pixel)

# Veriyi bir DataFrame'e dönüştür
df = pd.DataFrame(data, columns=["R", "G", "B"])

# DataFrame'i Excel'e dök
df.to_excel("output.xlsx", index=False)