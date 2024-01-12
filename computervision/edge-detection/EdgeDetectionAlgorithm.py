"""
 @author Seyit Ahmet ÖZDEMİR
 @project pytonworkspace EdgeDetectionAlgorithm
 @date 12 Oca 2024
 <p>
 @description: Canny ve Sobel kenar tespit algoritmalarının karşılştırıldığı bir uygulamadır.
 Treshold yöntemi olarak Otsu algoritması tercih edilmiştir.
"""
import tkinter as tk
import cv2
from tkinter import filedialog

import numpy as np
import pandas as pd
from PIL import Image, ImageTk

form = tk.Tk()
form.geometry("1500x800")
form.title("Görüntü İşleme - Canny ve Sobel Kenar Tespit Algoritması")

image = None
photo = None


def load_image():
    global image, photo, canny, sobel
    label = tk.Label
    try:
        imagePath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
        if len(imagePath) != 0:
            image = cv2.imread(imagePath)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            # Treshold oluşturmak için otsu algoritması kullanıldı.
            _, image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)))
            label = tk.Label(form, image=photo)
            label.grid(row=4, column=2, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=4)
            lblPath.config(text=imagePath)
            try:
                # Verileri depolamak için DataFrame oluştur
                df_image = pd.DataFrame(image)
                # Excel'e yazdır
                df_image.to_excel("treshold_gray_image.xlsx", index=False)
                lblProc.config(text=lblProc.cget("text") + "treshold_gray_image.xlsx oluşturuldu.\n")
            except Exception as e:
                lblProc.config(text=lblProc.cget("text") + "Excele aktarımda hata oluştu.\n")

    except Exception as e:
        lblPath.config(text="Resim yükleme hatası!")
        print(f"Hata: {e}")


def canny_algorithm():
    global image, canny
    canny = cv2.Canny(image, 50, 150)  # 50 ve 150, kenar tespiti için düşük ve yüksek eşik değerleridir

    canny_image_tk = ImageTk.PhotoImage(image=Image.fromarray(canny))

    label = tk.Label(form, image=canny_image_tk)
    label.image = canny_image_tk  # Referansı tutmak için
    label.grid(row=4, column=7, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=4)

    try:
        # Verileri depolamak için DataFrame oluştur
        df_canny = pd.DataFrame(canny)
        # Excel'e yazdır
        df_canny.to_excel("canny_image.xlsx", index=False)
        lblProc.config(text=lblProc.cget("text") + "canny_image.xlsx oluşturuldu.\n")
    except Exception as e:
        lblProc.config(text=lblProc.cget("text") + "Excele aktarımda hata oluştu!\n")


def sobel_algorithm():
    global image, sobel
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
    magnitude = np.sqrt(sobel_x ** 2 + sobel_y ** 2)

    sobel = np.uint8(magnitude)

    sobel_image_tk = ImageTk.PhotoImage(image=Image.fromarray(sobel))

    label = tk.Label(form, image=sobel_image_tk)
    label.image = sobel_image_tk  # Referansı tutmak için
    label.grid(row=4, column=12, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=4)

    try:
        # Verileri depolamak için DataFrame oluştur
        df_sobel = pd.DataFrame(sobel)
        # Excel'e yazdır
        df_sobel.to_excel("sobel_image.xlsx", index=False)
        lblProc.config(text=lblProc.cget("text") + "sobel_image.xlsx oluşturuldu.\n")
    except Exception as e:
        lblProc.config(text=lblProc.cget("text") + "Excele aktarımda hata oluştu!\n")


"""
Component yerleşimeri
"""
btnLoadImage = tk.Button(form, text="Resim Yükle", command=load_image)
btnLoadImage.grid(row=0, column=0, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

lblInfo = tk.Label(form, text="Seyit Ahmet ÖZDEMİR\n202285151045")
lblInfo.grid(row=0, column=1, padx=5, pady=5, sticky="w", rowspan=1, columnspan=1)

lblPath = tk.Label(form, text="-")
lblPath.grid(row=1, column=1, padx=5, pady=5, sticky="w", rowspan=1, columnspan=17)

btnCanny = tk.Button(form, text="Canny", command=canny_algorithm)
btnCanny.grid(row=2, column=0, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

btnSobel = tk.Button(form, text="Sobel", command=sobel_algorithm)
btnSobel.grid(row=3, column=0, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

lblProc = tk.Label(form, text="Süreç: \n")
lblProc.config(justify="left")
lblProc.grid(row=10, column=1, padx=5, pady=5, sticky="ws", rowspan=1, columnspan=17)

tk.mainloop()
