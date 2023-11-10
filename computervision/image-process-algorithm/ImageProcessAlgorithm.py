"""
 @author saozd
 @project pytonworkspace ImageProcessAlgorithm
 @date 10 Kas 2023
 <p>
 @description:50x50 görüntüyü görüntü işleme algoritmaları ile 20x20 ölçeklerine dönüştürecekuygulama
 Algoritmalar:
    1- INTER_NEAREST (En Yakın Komşu)
    2-INTER_AREA (Alan)
    3-INTER_CUBIC (Kübik)
    4-INTER_LINEAR (Doğrusal)
"""
import tkinter as tk
import cv2
from tkinter import filedialog
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pyplot as plt
import pandas as pd
import os

form = tk.Tk()
form.geometry("1024x600")
form.title("Görüntü İşleme Algoritmaları")

photo = None
label = None
image = None
resized = None
photoProc = None
labelProc = None
labelDesc = None


def show_photo_proc(resized):
    global photoProc, labelProc
    photoProc = ImageTk.PhotoImage(image=Image.fromarray(resized))
    labelProc = tk.Label(form, image=photoProc)
    labelProc.grid(row=4, column=2, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=1)
def inter_nearest():
    global resized
    resized = cv2.resize(image, (20, 20), interpolation=cv2.INTER_NEAREST)
    show_photo_proc(resized)
    print_to_excel("inter_nearest", 20, resized)

def inter_area():
    pass

def inter_cubic():
    pass

def inter_linear():
    pass

def show_image(image):
    global photo, label
    # normalImage = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    photo = ImageTk.PhotoImage(image=Image.fromarray(image))
    label = tk.Label(form, image=photo)
    label.grid(row=4, column=0, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=1)


def print_to_excel(name, size, img):
    # Matrisi oluştur
    matrix = []

    for i in range(size):
        row = []
        for j in range(size):
            pixel = img[i, j]
            row.append(pixel)
        matrix.append(row)

    # Veriyi bir DataFrame'e dönüştür
    df = pd.DataFrame(matrix, columns=[f'Pixel_{i}' for i in range(size)])
    df.index = [f'Pixel_{i}' for i in range(size)]

    if os.path.exists(name + ".xlsx"):
        os.remove(name + ".xlsx")

    # DataFrame'i Excel'e dök
    df.to_excel(name + ".xlsx", index=False)



def load_image():
    global image
    try:
        imagePath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
        if len(imagePath) != 0:
            image = cv2.imread(imagePath)
            image = cv2.resize(image, (50, 50))  # Yüklenen resmi 50x50 olacak şekilde resize et.
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            lblPath.config(text=imagePath)
            show_image(image)
            print_to_excel("normal", 50, image)
    except Exception as e:
        lblPath.config(text="Resim yükleme hatası!")
        print(f"Hata: {e}")

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

tk.mainloop()
