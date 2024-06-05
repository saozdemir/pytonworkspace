"""
 @author saozd
 @project pytonworkspace DlitaionErsionss
 @date 04 Oca 2024
 <p>
 @description:
"""
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

# RGB renk uzayına dönüştür
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
dilation_rgb = cv2.cvtColor(dilation, cv2.COLOR_BGR2RGB)
erosion_rgb = cv2.cvtColor(erosion, cv2.COLOR_BGR2RGB)

# Her pikselin RGB değerini [R:0 G:0 B:0] formatında bir liste oluştur
img_pixels = [[f"[R:{r} G:{g} B:{b}]" for r, g, b in row] for row in img_rgb]
dilation_pixels = [[f"[R:{r} G:{g} B:{b}]" for r, g, b in row] for row in dilation_rgb]
erosion_pixels = [[f"[R:{r} G:{g} B:{b}]" for r, g, b in row] for row in erosion_rgb]

# Listeleri DataFrame'e dönüştür
img_df = pd.DataFrame(img_pixels, columns=[f"Piksel {i}" for i in range(len(img_pixels[0]))])
dilation_df = pd.DataFrame(dilation_pixels, columns=[f"Piksel {i}" for i in range(len(dilation_pixels[0]))])
erosion_df = pd.DataFrame(erosion_pixels, columns=[f"Piksel {i}" for i in range(len(erosion_pixels[0]))])

# DataFrame'leri Excel dosyalarına kaydet
img_df.to_excel("orijinal.xlsx", index=False)
dilation_df.to_excel("dilation.xlsx", index=False)
erosion_df.to_excel("erosion.xlsx", index=False)

# Orijinal görüntüyü, Dilation işlemi uygulanmış görüntüyü ve Erosion işlemi uygulanmış görüntüyü ekranda göster
cv2.imshow("Orijinal", img)
cv2.imshow("Dilation", dilation)
cv2.imshow("Erosion", erosion)

# Pencereyi kapatmak için bir tuşa bas
cv2.waitKey(0)
cv2.destroyAllWindows()