"""
 @author saozd
 @project pytonworkspace ImageProcessAlgorithm
 @date 10 Kas 2023
 <p>
 @description:50x50 görüntüyü görüntü işleme algoritmaları ile 20x20 ölçeklerine dönüştürecekuygulama
 Algoritmalar:
    1-INTER_NEAREST (En Yakın Komşu)
    2-INTER_AREA (Alan)
    3-INTER_CUBIC (Kübik)
    4-INTER_LINEAR (Doğrusal)
"""
import math
import tkinter as tk
import cv2
from tkinter import filedialog
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pyplot as plt
import pandas as pd
import os

form = tk.Tk()
form.geometry("600x400")
form.title("Görüntü İşleme Algoritmaları")

photo = None
label = None
image = None
resized = None
photoProc = None
labelProc = None
labelDesc = None
matrix = None
MATRIX_SIZE = 50
NEW_MATRIX_SIZE = 20

"""Yüklenen fotoğrafı gösterir"""
def show_image(image):
    global photo, label
    # normalImage = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    photo = ImageTk.PhotoImage(image=Image.fromarray(image))
    label = tk.Label(form, image=photo)
    label.grid(row=4, column=0, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=1)


"""
İşlenmiş fotoğrafı gösterir.
"""
def show_photo_proc(resized):
    global photoProc, labelProc
    photoProc = ImageTk.PhotoImage(image=Image.fromarray(resized))
    labelProc = tk.Label(form, image=photoProc)
    labelProc.grid(row=4, column=2, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=1)

"""
Dosya Yükleme
"""
def load_image():
    global image
    try:
        imagePath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
        if len(imagePath) != 0:
            image = cv2.imread(imagePath)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            # image = cv2.resize(image, (50, 50))  # Yüklenen resmi 50x50 olacak şekilde resize et.
            # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            lblPath.config(text=imagePath)
            show_image(image)

    except Exception as e:
        lblPath.config(text="Resim yükleme hatası!")
        print(f"Hata: {e}")
    print_pixels_to_excel("normal", 50, image)

"""
Resmin piksellerinde bulunan RGB değerlerini bir matris olarka excel e aktarır.
"""
def print_pixels_to_excel(file_name, matrix_size, img):
    try:
        # Matrisi oluştur
        matrix = []

        for i in range(matrix_size):
            row = []
            for j in range(matrix_size):
                pixel = img[i, j]
                row.append(pixel)
            matrix.append(row)

        # Veriyi bir DataFrame'e dönüştür
        df = pd.DataFrame(matrix, columns=[f'Pixel_{i}' for i in range(matrix_size)])
        df.index = [f'Pixel_{i}' for i in range(matrix_size)]

        if os.path.exists(file_name + ".xlsx"):
            os.remove(file_name + ".xlsx")

        # DataFrame'i Excel'e dök
        df.to_excel(file_name + ".xlsx", index=False)
        lblExcel.config(text=file_name + " excel dosyası oluştruldu.")
    except Exception as e:
        lblPath.config(text="Excel hatası!")
        print(f"Hata: {e}")


"""
Yeniden boyutlandırma işleminde orjinal matristeki hangi piksel'in yeni matristeki değerine atanacağını
bir excel dosyasında oluşturarak gösterir.
"""
def print_resized_pixel_index_to_excel(file_name, matrix_size, new_matrix_size, img):
    global matrix
    size_ratio = float(matrix_size / new_matrix_size)
    matrix = [[f"({math.ceil(i * size_ratio)},{math.ceil(j * size_ratio)})" for j in range(new_matrix_size)] for i in
              range(new_matrix_size)]
    # matrix = [[f"({round(i * size_ratio)},{round(j * size_ratio)})" for j in range(new_matrix_size)] for i in
    #           range(new_matrix_size)]
    try:
        for i, row in enumerate(matrix):
            for j, element in enumerate(row):
                print(f"[m({i},{j}): {element}],", end=" ")
            print()
            # Veriyi bir DataFrame'e dönüştür
            df = pd.DataFrame(matrix, columns=[f'Pixel_{i}' for i in range(new_matrix_size)])
            df.index = [f'Pixel_{i}' for i in range(new_matrix_size)]

            if os.path.exists(file_name + ".xlsx"):
                os.remove(file_name + ".xlsx")

            # DataFrame'i Excel'e dök
            df.to_excel(file_name + ".xlsx", index=False)
            lblExcel.config(text=file_name + " excel dosyası oluştruldu.")
    except Exception as e:
        lblPath.config(text="Excel hatası!")
        print(f"Hata: {e}")


def inter_nearest():
    global resized, matrix
    size_ratio = float(MATRIX_SIZE / NEW_MATRIX_SIZE)
    resized = cv2.resize(image, (20, 20), interpolation=cv2.INTER_NEAREST)
    # resized = cv2.resize(image,None, fx=size_ratio, fy=size_ratio, interpolation=cv2.INTER_NEAREST)
    show_photo_proc(resized)
    matrix = [[f"({math.ceil(i * size_ratio)},{math.ceil(j * size_ratio)})" for j in range(NEW_MATRIX_SIZE)] for i in
              range(NEW_MATRIX_SIZE)]
    # matrix = [[f"({round(i * size_ratio)},{round(j * size_ratio)})" for j in range(NEW_MATRIX_SIZE)] for i in
    #           range(NEW_MATRIX_SIZE)]
    print_resized_pixel_index_to_excel("inter_nearest_index", 50, 20, resized)
    print_pixels_to_excel("inter_nearest", 20, resized)


def inter_area():
    global resized
    resized = cv2.resize(image, (20, 20), interpolation=cv2.INTER_AREA)
    show_photo_proc(resized)
    print_pixels_to_excel("inter_area", 20, resized)


def inter_cubic():
    global resized
    resized = cv2.resize(image, (20, 20), interpolation=cv2.INTER_CUBIC)
    show_photo_proc(resized)
    print_pixels_to_excel("inter_cubic", 20, resized)
    print_resized_pixel_index_to_excel("inter_cubic_resized", 50, 20, resized)


def inter_linear():
    global resized
    resized = cv2.resize(image, (20, 20), interpolation=cv2.INTER_LINEAR)
    show_photo_proc(resized)
    print_pixels_to_excel("inter_linear", 20, resized)

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
