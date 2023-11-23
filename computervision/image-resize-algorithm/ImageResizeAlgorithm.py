"""
 @author saozd
 @project pytonworkspace ImageResizeAlgorithm
 @date 10 Kas 2023
 <p>
 @description:50x50 görüntüyü görüntü işleme algoritmaları ile 20x20 ölçeklerine dönüştürecekuygulama
 Algoritmalar:
    1-INTER_NEAREST (En Yakın Komşu)
    2-INTER_AREA (Alan)
    3-INTER_CUBIC (Kübik)
    4-INTER_LINEAR (Doğrusal)
"""
import tkinter as tk
import cv2
from tkinter import filedialog
from PIL import Image, ImageTk
import pandas as pd

form = tk.Tk()
form.geometry("600x400")
form.title("Görüntü İşleme Algoritmaları")

image = None
gray_image = None
photo = None
label = None
resized_label = None
resized_image_inter_nearest=None
resized_image_inter_area=None
resized_image_inter_cubic=None
resized_image_inter_linear=None

def load_image():
    global image, gray_image
    try:
        imagePath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
        if len(imagePath) != 0:
            image = cv2.imread(imagePath)
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            lblPath.config(text=imagePath)
            show_image(image)
            # Verileri depolamak için DataFrame oluştur
            df_original = pd.DataFrame(gray_image)

            # Excel'e yazdır
            df_original.to_excel("original_64x64.xlsx", index=False)

    except Exception as e:
        lblPath.config(text="Resim yükleme hatası!")
        print(f"Hata: {e}")

def show_image(image):
    global photo, label
    photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)))
    label = tk.Label(form, image=photo)
    label.grid(row=4, column=0, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=1)

def inter_nearest():
    global gray_image, resized_label,resized_image_inter_nearest

    # INTER_NEAREST algoritması ile resmi 16x16 boyutuna küçült
    resized_inter_nearest = cv2.resize(gray_image, (16, 16), interpolation=cv2.INTER_NEAREST)

    # Verileri depolamak için DataFrame oluştur
    df_resized = pd.DataFrame(resized_inter_nearest)

    # Excel'e yazdır
    df_resized.to_excel("resized_inter_nearest.xlsx", index=False)

    resized_image_inter_nearest = ImageTk.PhotoImage(image=Image.fromarray(resized_inter_nearest))
    resized_label = tk.Label(form, image=resized_image_inter_nearest)
    resized_label.grid(row=4, column=2, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=1)

def inter_area():
    global gray_image, resized_label,resized_image_inter_area

    # INTER_AREA algoritması ile resmi 16x16 boyutuna küçült
    resized_inter_area = cv2.resize(gray_image, (16, 16), interpolation=cv2.INTER_AREA)

    # Verileri depolamak için DataFrame oluştur
    df_resized = pd.DataFrame(resized_inter_area)

    # Excel'e yazdır
    df_resized.to_excel("resized_inter_area.xlsx", index=False)

    resized_image_inter_area = ImageTk.PhotoImage(image=Image.fromarray(resized_inter_area))
    resized_label = tk.Label(form, image=resized_image_inter_area)
    resized_label.grid(row=4, column=2, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=1)
def inter_cubic():
    global gray_image, resized_label, resized_image_inter_cubic

    # INTER_CUBIC algoritması ile resmi 16x16 boyutuna küçült
    resized_inter_cubic = cv2.resize(gray_image, (16, 16), interpolation=cv2.INTER_CUBIC)

    # Verileri depolamak için DataFrame oluştur
    df_resized = pd.DataFrame(resized_inter_cubic)

    # Excel'e yazdır
    df_resized.to_excel("resized_inter_cubic.xlsx", index=False)

    resized_image_inter_cubic = ImageTk.PhotoImage(image=Image.fromarray(resized_inter_cubic))
    resized_label = tk.Label(form, image=resized_image_inter_cubic)
    resized_label.grid(row=4, column=2, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=1)
def inter_linear():
    global gray_image, resized_label, resized_image_inter_linear

    # INTER_LINEAR algoritması ile resmi 16x16 boyutuna küçült
    resized_inter_linear = cv2.resize(gray_image, (16, 16), interpolation=cv2.INTER_LINEAR)

    # Verileri depolamak için DataFrame oluştur
    df_resized = pd.DataFrame(resized_inter_linear)

    # Excel'e yazdır
    df_resized.to_excel("resized_inter_linear.xlsx", index=False)

    resized_image_inter_linear = ImageTk.PhotoImage(image=Image.fromarray(resized_inter_linear))
    resized_label = tk.Label(form, image=resized_image_inter_linear)
    resized_label.grid(row=4, column=2, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=1)

"""
Component yerleşimeri
"""
btnLoadImage = tk.Button(form, text="Resim Yükle", command=load_image)
btnLoadImage.grid(row=0, column=0, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

btnInterNearest = tk.Button(form, text="Inter Nearest", command=inter_nearest)
btnInterNearest.grid(row=0, column=1, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

btnInterArea = tk.Button(form, text="Inter Area", command=inter_area)
btnInterArea.grid(row=0, column=2, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

btnInterCubic = tk.Button(form, text="Inter Cubic", command=inter_cubic)
btnInterCubic.grid(row=0, column=3, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

btnInterLinear = tk.Button(form, text="Inter Linear", command=inter_linear)
btnInterLinear.grid(row=0, column=4, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

lblPath = tk.Label(form, text="-")
lblPath.grid(row=2, column=0, padx=5, pady=5, sticky="w", rowspan=1, columnspan=8)

lblInfo = tk.Label(form, text="Seyit Ahmet ÖZDEMİR\n202285151045")
lblInfo.grid(row=3, column=0, padx=5, pady=5, sticky="w", rowspan=1, columnspan=6)

lblExcel = tk.Label(form, text="-")
lblExcel.grid(row=5, column=0, padx=5, pady=5, sticky="w", rowspan=1, columnspan=6)

tk.mainloop()
