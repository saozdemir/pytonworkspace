"""
 @author Seyit Ahmet ÖZDEMİR
 @project pytonworkspace DilationAndErosion
 @date 04 Oca 2024
 <p>
 @description:Dilation ve Erosyon işlemlerini uygulayan algoritma
"""
import tkinter as tk
import cv2
from tkinter import filedialog

import numpy as np
import pandas as pd
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pyplot as plt

form = tk.Tk()
form.geometry("1024x600")
form.title("Görüntü İşleme - Dilation Erosion")

photo = None
label = None
image = None
photoProc = None
labelProc = None
labelDesc = None

dilationImage = None
dilationPhoto = None
lblDilation = None

erosionImage = None
erosionPhoto = None
lblErosion= None

"""
Yüklenen fotoğrafı gösterir
"""
def show_image(image):
    global photo, label
    normalImage = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    photo = ImageTk.PhotoImage(image=Image.fromarray(normalImage))
    label = tk.Label(form, image=photo)
    label.grid(row=6, column=0, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=8)


"""
Yapılan işlemi yazdırır.
"""
def show_process_description(text):
    global labelDesc
    labelDesc = tk.Label(form, text=text)
    labelDesc.grid(row=2, column=7, padx=5, pady=5, sticky="w", rowspan=1, columnspan=2)

"""
FileDialog ile resim seçimini alır
"""
def load_image():
    global image
    try:
        imagePath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
        if len(imagePath) != 0:
            image = cv2.imread(imagePath)
            # image = cv2.resize(image, (300, 300))  # Yüklenen resmi 300x300 olacak şekilde resize et.
            lblPath.config(text=imagePath)
            show_image(image)
            img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            # Her pikselin RGB değerini [R:0 G:0 B:0] formatında bir liste oluştur
            img_pixels = [[f"[R:{r} G:{g} B:{b}]" for r, g, b in row] for row in img_rgb]
            # Listeleri DataFrame'e dönüştür
            img_df = pd.DataFrame(img_pixels, columns=[f"Piksel {i}" for i in range(len(img_pixels[0]))])
            # DataFrame'leri Excel dosyalarına kaydet
            img_df.to_excel("orijinal.xlsx", index=False)
    except Exception as e:
        lblPath.config(text="Resim yükleme hatası!")
        print(f"Hata: {e}")

def dilation():
    global image, dilationImage, dilationPhoto
    dilationInfo=""
    # Yapısal element oluştur
    kernel = np.ones((5, 5), np.uint8)

    # Dilation işlemi uygula
    dilationImage = cv2.dilate(image, kernel, iterations=1)

    # Orijinal görüntünün piksel sayısını bul
    original_area = np.sum(image) / 255
    dilationInfo = dilationInfo + "Orijinal görüntünün alanı:" + str(original_area) + "piksel\n"

    # Dilation işlemi uygulanmış görüntünün piksel sayısını bul
    dilation_area = np.sum(dilationImage) / 255
    dilationInfo = dilationInfo + "Dilation işlemi uygulanmış görüntünün alanı:"+ str(dilation_area) + "piksel\n"

    dilationInfo = dilationInfo + f"Dilation işlemi, orijinal görüntünün alanını %{((dilation_area - original_area) / original_area) * 100:.2f} oranında artırmıştır.\n"

    dilation_rgb = cv2.cvtColor(dilationImage, cv2.COLOR_BGR2RGB)

    dilation_pixels = [[f"[R:{r} G:{g} B:{b}]" for r, g, b in row] for row in dilation_rgb]
    # Verileri depolamak için DataFrame oluştur
    dilation_df = pd.DataFrame(dilation_pixels, columns=[f"Piksel {i}" for i in range(len(dilation_pixels[0]))])

    # Excel'e yazdır
    dilation_df.to_excel("dilation.xlsx", index=False)

    dilationPhoto = ImageTk.PhotoImage(image=Image.fromarray(dilation_rgb))
    lblDilation = tk.Label(form, image=dilationPhoto)
    lblDilation.grid(row=7, column=0, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=8)
    lblDilationInfo = tk.Label(form, text=dilationInfo)
    lblDilationInfo.grid(row=7, column=9, padx=5, pady=5, sticky="w", rowspan=1, columnspan=4)

def erosion():
    global image, erosionImage, erosionPhoto
    erosionInfo = ""
    # Yapısal element oluştur
    kernel = np.ones((5, 5), np.uint8)

    # Erosion işlemi uygula
    erosionImage = cv2.erode(image, kernel, iterations=1)

    # Orijinal görüntünün piksel sayısını bul
    original_area = np.sum(image) / 255
    erosionInfo = erosionInfo + "Orijinal görüntünün alanı:" + str(original_area) + "piksel\n"

    # Erosion işlemi uygulanmış görüntünün piksel sayısını bul
    erosion_area = np.sum(erosionImage) / 255
    erosionInfo = erosionInfo + "Erosion işlemi uygulanmış görüntünün alanı:" + str(erosion_area) + "piksel\n"

    erosionInfo = erosionInfo + f"Erosion işlemi, orijinal görüntünün alanını %{((original_area - erosion_area) / original_area) * 100:.2f} oranında azaltmıştır.\n"

    erosion_rgb = cv2.cvtColor(erosionImage, cv2.COLOR_BGR2RGB)

    erosion_pixels = [[f"[R:{r} G:{g} B:{b}]" for r, g, b in row] for row in erosion_rgb]
    # Verileri depolamak için DataFrame oluştur
    erosion_df = pd.DataFrame(erosion_pixels, columns=[f"Piksel {i}" for i in range(len(erosion_pixels[0]))])

    # Excel'e yazdır
    erosion_df.to_excel("erosion.xlsx", index=False)

    erosionPhoto = ImageTk.PhotoImage(image=Image.fromarray(erosion_rgb))
    lblErosion = tk.Label(form, image=erosionPhoto)
    lblErosion.grid(row=8, column=0, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=8)
    lblErosionInfo = tk.Label(form, text=erosionInfo)
    lblErosionInfo.grid(row=8, column=9, padx=5, pady=5, sticky="w", rowspan=1, columnspan=4)

"""
Component yerleşimeri
"""
btnLoadImage = tk.Button(form, text="Resim Yükle", command=load_image)
btnLoadImage.grid(row=0, column=0, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

btnDilation = tk.Button(form, text="Dilation", command=dilation)
btnDilation.grid(row=0, column=1, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

btnErosion = tk.Button(form, text="Erosion", command=erosion)
btnErosion.grid(row=0, column=2, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

lblPath = tk.Label(form, text="-")
lblPath.grid(row=0, column=9, padx=5, pady=5, sticky="w", rowspan=1, columnspan=6)

lblInfo = tk.Label(form, text="Seyit Ahmet ÖZDEMİR\n202285151045")
lblInfo.grid(row=0, column=4, padx=5, pady=5, sticky="w", rowspan=1, columnspan=4)

tk.mainloop()