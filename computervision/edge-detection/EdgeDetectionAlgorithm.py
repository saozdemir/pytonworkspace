"""
 @author Seyit Ahmet ÖZDEMİR
 @project pytonworkspace EdgeDetectionAlgorithm
 @date 12 Oca 2024
 <p>
 @description: Canny ve Sobel kenar tespit algoritmalarının karşılştırıldığı bir uygulamadır.
    Pazariz azaltma için "Gaussian Blur" algoritması tercih edilmiştir.
    Treshold yöntemi olarak Otsu algoritması tercih edilmiştir.
"""
import tkinter as tk
import cv2
from tkinter import filedialog

import numpy as np
import pandas as pd
from PIL import Image, ImageTk

form = tk.Tk()
form.geometry("1600x800")
form.title("Görüntü İşleme - Canny ve Sobel Kenar Tespit Algoritması")

image = None
photo = None
photo_original = None


def load_image():
    global image, photo, photo_original, canny, sobel
    label = tk.Label
    label_original = tk.Label
    try:
        imagePath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
        if len(imagePath) != 0:
            image = cv2.imread(imagePath)
            lblProc.config(text=lblProc.cget("text") + "Orjinal resim yüklendi.\n")

            # Orjinal fotoğrafı göster
            photo_original = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)))
            label_original = tk.Label(form, image=photo_original)
            label_original.grid(row=5, column=2, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=4)

            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Resimdeki parazitleri azaltmak için gaussian blur işlemi uygulandı.
            image = cv2.GaussianBlur(image, (5, 5), 1, 0, 1)
            lblProc.config(text=lblProc.cget("text") + "Gaussian Blur algoritması uygulandı.\n")

            # Treshold oluşturmak için otsu algoritması kullanıldı.
            _, image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            lblProc.config(text=lblProc.cget("text") + "Otsu Treshold algoritması uygulandı.\n")

            photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)))
            label = tk.Label(form, image=photo)
            label.grid(row=5, column=7, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=4)
            lblPath.config(text=imagePath)
            try:
                # Verileri depolamak için DataFrame oluşturuldu ve blurlanmış ve gri tonlamaya dönüşmüş resim uygulandı.
                df_image = pd.DataFrame(image)
                # Excel'e yazdır
                df_image.to_excel("treshold_gray_image.xlsx", index=False)
                lblProc.config(text=lblProc.cget("text") + "Gri Tonlama : treshold_gray_image.xlsx oluşturuldu.\n")
            except Exception as e:
                lblProc.config(text=lblProc.cget("text") + "Excele aktarımda hata oluştu.\n")

    except Exception as e:
        lblPath.config(text="Resim yükleme hatası!")
        print(f"Hata: {e}")


def canny_algorithm():
    global image, canny

    # Canny kenar tespiti
    canny = cv2.Canny(image, 50, 150)  # 50 ve 150, kenar tespiti için düşük ve yüksek eşik değerleridir

    canny_image_tk = ImageTk.PhotoImage(image=Image.fromarray(canny))

    label = tk.Label(form, image=canny_image_tk)
    label.image = canny_image_tk  # Referansı tutmak için
    label.grid(row=5, column=12, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=4)

    try:
        # Verileri depolamak için DataFrame oluşturuldu ve Canny kenar tespit algoritması uygulandı.
        df_canny = pd.DataFrame(canny)
        # Excel'e yazdır
        df_canny.to_excel("canny_image.xlsx", index=False)
        lblProc.config(text=lblProc.cget("text") + "Canny: canny_image.xlsx oluşturuldu.\n")
    except Exception as e:
        lblProc.config(text=lblProc.cget("text") + "Excele aktarımda hata oluştu!\n")


def sobel_algorithm():
    global image, sobel

    #
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
    magnitude = np.sqrt(sobel_x ** 2 + sobel_y ** 2)

    sobel = np.uint8(magnitude)

    sobel_image_tk = ImageTk.PhotoImage(image=Image.fromarray(sobel))

    label = tk.Label(form, image=sobel_image_tk)
    label.image = sobel_image_tk  # Referansı tutmak için
    label.grid(row=5, column=17, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=4)

    try:
        # Verileri depolamak için DataFrame oluşturuldu ve Sobel kenar tespit algoritması uygulandı.
        df_sobel = pd.DataFrame(sobel)
        # Excel'e yazdır
        df_sobel.to_excel("sobel_image.xlsx", index=False)
        lblProc.config(text=lblProc.cget("text") + "Sobel : sobel_image.xlsx oluşturuldu.\n")
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

lblOriginal = tk.Label(form, text="Orjinal Resim")
lblOriginal.config(justify="left")
lblOriginal.grid(row=4, column=2, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=4)

lblGray = tk.Label(form, text="Gri Resim \n(Gaussian Blur + Otsu)")
lblGray.config(justify="left")
lblGray.grid(row=4, column=7, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=4)

lblOriginal = tk.Label(form, text="Canny Kenar Tespiti")
lblOriginal.config(justify="left")
lblOriginal.grid(row=4, column=12, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=4)

lblOriginal = tk.Label(form, text="Sobel Kenar Tespiti")
lblOriginal.config(justify="left")
lblOriginal.grid(row=4, column=16, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=4)

tk.mainloop()
