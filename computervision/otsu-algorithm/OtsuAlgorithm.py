"""
 @author Seyit Ahmet ÖZDEMİR
 @project pytonworkspace OtsuAlgorithm
 @date 19 Ara 2023
 <p>
 @description: Otsu Threshholding Algoritmasının Uygulaması
"""
import tkinter as tk
import cv2
from tkinter import filedialog

from PIL import Image, ImageTk

form = tk.Tk()
form.geometry("600x400")
form.title("Otsu Algoritması")

image = None
photo = None
gray_image = None
thresholded_image = None
otsu_image = None


def load_image():
    global image, photo
    try:
        imagePath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
        if len(imagePath) != 0:
            image = cv2.imread(imagePath)
            photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)))
            label = tk.Label(form, image=photo)
            label.grid(row=4, column=0, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=1)

    except Exception as e:
        lblPath.config(text="Resim yükleme hatası!")
        print(f"Hata: {e}")


def traditional_gray_scale():
    global image, gray_image, photo, thresholded_image
    # gray_image = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)))
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Geleneksel eşikleme işlemi uygula
    threshold_value = 127 # manuel girildi
    _, thresholded_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)

    gray_image_tk = ImageTk.PhotoImage(image=Image.fromarray(thresholded_image))
    label = tk.Label(form, image=gray_image_tk)
    label.image = gray_image_tk  # Referansı tutmak için
    label.grid(row=4, column=1, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=1)


def otsu_thresholding():
    global image, photo, gray_image, otsu_image
    gray_image_cv = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, otsu_image = cv2.threshold(gray_image_cv, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Otsu thresholding işlemi sonrasında elde edilen görüntüyü Tkinter PhotoImage formatına çevir
    otsu_image_tk = ImageTk.PhotoImage(image=Image.fromarray(otsu_image))

    label = tk.Label(form, image=otsu_image_tk)
    label.image = otsu_image_tk  # Referansı tutmak için
    label.grid(row=4, column=2, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=1)


"""
Component yerleşimeri
"""
btnLoadImage = tk.Button(form, text="Resim Yükle", command=load_image)
btnLoadImage.grid(row=0, column=0, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

btnGrayScale = tk.Button(form, text="Geleneksel Gri Tonlama", command=traditional_gray_scale)
btnGrayScale.grid(row=0, column=1, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

btnLoadTemplate = tk.Button(form, text="Otsu Algoritması", command=otsu_thresholding)
btnLoadTemplate.grid(row=0, column=2, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

lblPath = tk.Label(form, text="-")
lblPath.grid(row=2, column=0, padx=5, pady=5, sticky="w", rowspan=1, columnspan=8)

lblInfo = tk.Label(form, text="Seyit Ahmet ÖZDEMİR\n202285151045")
lblInfo.grid(row=3, column=0, padx=5, pady=5, sticky="w", rowspan=1, columnspan=6)

tk.mainloop()
