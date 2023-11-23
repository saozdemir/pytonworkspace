"""
 @author saozd
 @project pytonworkspace MatchTemplateAlgorithm
 @date 20 Kas 2023
 <p>
 @description: matchTemplate nesne tanımlama algoritması için bir uygulama
"""
import tkinter as tk
import cv2
from tkinter import filedialog

import numpy as np
from PIL import Image, ImageTk
import pandas as pd

form = tk.Tk()
form.geometry("600x400")
form.title("Nesne Tanımlama Algoritması (matchTemplate)")

image = None
gray_image = None
template = None
gray_image_template = None
photoTemplate = None
lblTemplate = None
photoMatch = None
lblMatch = None


def load_image():
    global image, gray_image
    try:
        imagePath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
        if len(imagePath) != 0:
            image = cv2.imread(imagePath)
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            # lblPath.config(text=imagePath)
            show_image(image)
            # Verileri depolamak için DataFrame oluştur
            df_original = pd.DataFrame(gray_image)

            # Excel'e yazdır
            df_original.to_excel("original_64x64.xlsx", index=False)

    except Exception as e:
        lblPath.config(text="Resim yükleme hatası!")
        print(f"Hata: {e}")


def load_template_image():
    global template, gray_image_template
    try:
        imagePath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
        if len(imagePath) != 0:
            template = cv2.imread(imagePath)
            gray_image_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
            # lblPath.config(text=imagePath)
            show_template_image(gray_image_template)
            # Verileri depolamak için DataFrame oluştur
            df_template = pd.DataFrame(gray_image)

            # Excel'e yazdır
            df_template.to_excel("template.xlsx", index=False)

    except Exception as e:
        lblPath.config(text="Resim yükleme hatası!")
        print(f"Hata: {e}")


def show_image(image):
    global photo, label
    photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)))
    label = tk.Label(form, image=photo)
    label.grid(row=4, column=0, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=1)


def show_template_image(gray_image_template):
    global photoTemplate, lblTemplate
    photoTemplate = ImageTk.PhotoImage(image=Image.fromarray(gray_image_template))
    lblTemplate = tk.Label(form, image=photoTemplate)
    lblTemplate.grid(row=4, column=2, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=1)

def match_template():
    global gray_image, gray_image_template, photoMatch, lblMatch

    # Korelasyon matrisi
    I_normalized = (gray_image - np.mean(gray_image)) / np.std(gray_image)
    T_normalized = (gray_image_template - np.mean(gray_image_template)) / np.std(gray_image_template)

    # Korelasyon hesaplama
    correlation_matrix = np.correlate(I_normalized.flatten(), T_normalized.flatten(), mode='full')

    # Korelasyon matrisini yeniden boyutlandırma
    correlation_matrix = np.resize(correlation_matrix,
                                   (gray_image.shape[0] - gray_image_template.shape[0] + 1, gray_image.shape[1] - gray_image_template.shape[1] + 1))

    # Şablonun boyutlarını al
    h, w = gray_image_template.shape[:2]

    # Eşleştirme yöntemini seç (örneğin, cv2.TM_CCOEFF_NORMED kullanılabilir)
    method = cv2.TM_CCOEFF_NORMED  # korelasyon katsayısını normal şekilde kullanır

    # Eşleştirmeyi gerçekleştir
    result = cv2.matchTemplate(gray_image, gray_image_template, method)

    # Belirli bir eşik değeri üzerindeki eşleşmeleri bul
    threshold = 0.8
    loc = np.where(result >= threshold)

    # Tüm eşleşmeleri işaretle
    for pt in zip(*loc[::-1]):
        top_left = pt
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(gray_image, top_left, bottom_right, (0, 255, 0), 1)

    # Eşik değerini geçen piksellerin konumlarını bulma
    matching_points = np.where(correlation_matrix >= threshold)

    # Verileri depolamak için DataFrame oluştur
    df_gray_image = pd.DataFrame(gray_image)
    df_gray_image_template = pd.DataFrame(gray_image_template)
    df_correlation_matrix = pd.DataFrame(correlation_matrix)
    df_matching_points = pd.DataFrame(list(zip(matching_points[1], matching_points[0])), columns=['X', 'Y'])

    # Excel'e yazdır
    df_gray_image_template.to_excel("gray_image_template.xlsx", index=False)
    df_correlation_matrix.to_excel("correlation_matrix.xlsx", index=False)
    df_matching_points.to_excel("matching_points.xlsx", index=False)

    df_with_matching_points = pd.concat([df_gray_image, df_matching_points], axis=1)
    df_with_matching_points.to_excel("gray_image_matching_points.xlsx", index=False)

    # Görüntü işaretledi. İşaretlenmiş görüntüyü göster
    photoMatch = ImageTk.PhotoImage(image=Image.fromarray(gray_image))
    lblMatch = tk.Label(form, image=photoMatch)
    lblMatch.grid(row=4, column=4, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=1)
    pass

"""
Component yerleşimeri
"""
btnLoadImage = tk.Button(form, text="Resim Yükle", command=load_image)
btnLoadImage.grid(row=0, column=0, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

btnLoadTemplate = tk.Button(form, text="Aranacak Görüntü", command=load_template_image)
btnLoadTemplate.grid(row=0, column=1, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

btnMatchTemplate = tk.Button(form, text="Match Template", command=match_template)
btnMatchTemplate.grid(row=0, column=2, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

lblPath = tk.Label(form, text="-")
lblPath.grid(row=2, column=0, padx=5, pady=5, sticky="w", rowspan=1, columnspan=8)

lblInfo = tk.Label(form, text="Seyit Ahmet ÖZDEMİR\n202285151045")
lblInfo.grid(row=3, column=0, padx=5, pady=5, sticky="w", rowspan=1, columnspan=6)

lblExcel = tk.Label(form, text="-")
lblExcel.grid(row=5, column=0, padx=5, pady=5, sticky="w", rowspan=1, columnspan=6)

tk.mainloop()
