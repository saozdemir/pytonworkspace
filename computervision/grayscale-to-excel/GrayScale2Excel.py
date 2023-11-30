"""
 @author Seyit Ahmet ÖZDEMİR
 @project pytonworkspace GrayScale2Excel
 @date 30 Kas 2023
 <p>
 @description: 1024x768 boyutunda bir görüntüyü gri tonlamaya dönüştürerek piksel değerlerini excel'e yazdıran kod örneği
"""
import tkinter as tk
import cv2
import pandas as pd
from tkinter import filedialog
from PIL import Image, ImageTk

form = tk.Tk()
form.geometry("1080x700")
form.title("Gray Scale Pixel")

image = None
gray_image = None
photo = None
label = None
lblExcel = None

def load_image():
    global image, gray_image
    lblPath.config(text="-")
    try:
        imagePath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
        if len(imagePath) != 0:
            image = cv2.imread(imagePath)
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            lblPath.config(text=imagePath)
            show_image(image)
    except Exception as e:
        lblPath.config(text="Resim yükleme hatası!")
        print(f"Hata: {e}")


def show_image(image):
    global photo, label
    photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)))
    label = tk.Label(form, image=photo)
    label.grid(row=3, column=0, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=12)

def print_to_excel():
    global gray_image, lblExcel
    lblExcel.config(text="-")
    try:
        # Verileri depolamak için DataFrame oluştur
        df_gray_image = pd.DataFrame(gray_image)
        # Excel'e yazdır
        df_gray_image.to_excel("gray_scale_1024x576.xlsx", index=False)
        lblExcel.config(text="gray_scale_1024x576.xlsx oluşturuldu.")
    except Exception as e:
        lblExcel.config(text="Excele aktarımda hata oluştu!")

btnLoadImage = tk.Button(form, text="Resim Yükle", command=load_image)
btnLoadImage.grid(row=0, column=0, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

btnInterNearest = tk.Button(form, text="Gri Tonlamayı Excel' Aktar", command=print_to_excel)
btnInterNearest.grid(row=0, column=1, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

lblPath = tk.Label(form, text="-")
lblPath.grid(row=1, column=0, padx=5, pady=5, sticky="w", rowspan=1, columnspan=6)

lblExcel = tk.Label(form, text="-")
lblExcel.grid(row=1, column=7, padx=5, pady=5, sticky="w", rowspan=1, columnspan=6)

tk.mainloop()
