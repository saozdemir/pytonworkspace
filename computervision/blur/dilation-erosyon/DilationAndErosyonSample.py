"""
 @author saozd
 @project pytonworkspace DilationAndErosyonSample
 @date 02 Oca 2024
 <p>
 @description:
"""
# OpenCV ve numpy kütüphanelerini içe aktar
import cv2
import os
import numpy as np
import pandas as pd


resource_root = r'E:\PycharmProjects\pytonworkspace\computervision\blur\resources'

# Görüntüleri oku
img1_path = os.path.join(resource_root, 'sample_image.PNG')
# Bir resmi oku
img = cv2.imread(img1_path)
# Yapısal element oluştur
kernel = np.ones((5, 5), np.uint8)

# Dilation işlemi uygula
dilation = cv2.dilate(img, kernel, iterations=1)

# Erosion işlemi uygula
erosion = cv2.erode(img, kernel, iterations=1)


# Orijinal görüntünün piksel sayısını bul
original_area = np.sum(img) / 255
print("Orijinal görüntünün alanı:", original_area, "piksel")

# Dilation işlemi uygulanmış görüntünün piksel sayısını bul
dilation_area = np.sum(dilation) / 255
print("Dilation işlemi uygulanmış görüntünün alanı:", dilation_area, "piksel")

# Erosion işlemi uygulanmış görüntünün piksel sayısını bul
erosion_area = np.sum(erosion) / 255
print("Erosion işlemi uygulanmış görüntünün alanı:", erosion_area, "piksel")

# Alan kıyaslaması yap
print("Dilation işlemi, orijinal görüntünün alanını %", ((dilation_area - original_area) / original_area) * 100, "oranında artırmıştır.")
print("Erosion işlemi, orijinal görüntünün alanını %", ((original_area - erosion_area) / original_area) * 100, "oranında azaltmıştır.")


# Görüntüleri Bitmap formatına dönüştür
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
dilation_rgb = cv2.cvtColor(dilation, cv2.COLOR_BGR2RGB)
erosion_rgb = cv2.cvtColor(erosion, cv2.COLOR_BGR2RGB)




# Renk kanallarını ayır
img_channels = cv2.split(img_rgb)
dilation_channels = cv2.split(dilation_rgb)
erosion_channels = cv2.split(erosion_rgb)

# # Görüntülerin renk değerlerini bir veri çerçevesine dönüştür
# img_df = pd.DataFrame(img_rgb.reshape(-1, 3), columns=["Kırmızı", "Yeşil", "Mavi"])
# dilation_df = pd.DataFrame(dilation_rgb.reshape(-1, 3), columns=["Kırmızı", "Yeşil", "Mavi"])
# erosion_df = pd.DataFrame(erosion_rgb.reshape(-1, 3), columns=["Kırmızı", "Yeşil", "Mavi"])

# Renk kanallarını birleştirip yeniden şekillendir
img_flat = np.column_stack(img_channels).reshape(-1, 3)

# Görüntülerin renk değerlerini bir veri çerçevesine dönüştür
img_df = pd.DataFrame({"RGB: ": [f"[R:{r} G:{g} B:{b}]" for r, g, b in img_flat]})
# dilation_df = pd.DataFrame(dilation_rgb.reshape(-1, 3), columns=["Kırmızı", "Yeşil", "Mavi"])
# erosion_df = pd.DataFrame(erosion_rgb.reshape(-1, 3), columns=["Kırmızı", "Yeşil", "Mavi"])

# Veri çerçevelerini Excel dosyalarına kaydet
img_df.to_excel("orijinal.xlsx", index=False)
# dilation_df.to_excel("dilation.xlsx", index=False)
# erosion_df.to_excel("erosion.xlsx", index=False)

# Orijinal görüntüyü, Dilation işlemi uygulanmış görüntüyü ve Erosyon işlemi uygulanmış görüntüyü ekranda göster
cv2.imshow("Orijinal", img)
cv2.imshow("Dilation", dilation)
cv2.imshow("Erosion", erosion)

# Pencereyi kapatmak için bir tuşa bas
cv2.waitKey(0)
cv2.destroyAllWindows()