"""
#author: saozdemir
#description: Görüntü İşleme Uygulaması

"""

import tkinter as tk
import cv2
from tkinter import filedialog
from PIL import Image, ImageTk

form = tk.Tk()
form.geometry("700x700")
form.title("Görüntü İşleme")

"""
Yüklenen resmin pixellerini yazdıracak metot.
"""
def print_image_pixel(image):
    for i, row in enumerate(image):
        for j, pixel in enumerate(row):
            blue, green, red = pixel
            print(f"pixel({i},{j}) = [{red},{green},{blue}]")
    print("Done")


"""
FileDialog ile resim seçimini alır
Alınan resmi 300x300px formatına resize eder.
"""
photo = None
label = None
image = None
photoProc = None
labelProc = None

def show_image(image):
    global photo, label
    normalImage = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    photo = ImageTk.PhotoImage(image=Image.fromarray(normalImage))
    label = tk.Label(form, image=photo)
    label.grid(row=2, column=0, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=4)

def show_processed_image(matrix):
    global photoProc, labelProc
    photoProc = ImageTk.PhotoImage(image=Image.fromarray(matrix))
    labelProc = tk.Label(form, image=photoProc)
    labelProc.grid(row=2, column=4, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=4)

"""
Yüklenen foroğrafı tersler eder.
"""
def invert():
    global photoProc, labelProc
    matrix = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(matrix.shape[2]):
                matrix[i, j, k] = max(0, 255 - matrix[i, j, k])

    show_processed_image(matrix)

"""
Yüklenen fotoğrafı karartır.
"""
def darken():
    global photoProc, labelProc
    matrix = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(matrix.shape[2]):
                matrix[i, j, k] = max(0, matrix[i, j, k] - 128)
    show_processed_image(matrix)

"""
Yüklenen fotoğrafı aydınlatır.
"""
def lighten():
    global photoProc, labelProc
    matrix = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(matrix.shape[2]):
                matrix[i, j, k] = min(255, matrix[i, j, k] + 128)
    show_processed_image(matrix)


"""
Yüklenen fotoğrafın kotrastını düşürür.
"""
def lower_cont():
    global photoProc, labelProc
    matrix = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(matrix.shape[2]):
                matrix[i, j, k] = round(matrix[i, j, k] /2)
    show_processed_image(matrix)

"""
Yüklenen fotoğrafın kotrastını artırır.
"""
def raise_cont():
    global photoProc, labelProc
    matrix = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(matrix.shape[2]):
                matrix[i, j, k] = min(255, matrix[i, j, k] * 2)
    show_processed_image(matrix)

"""
Yüklenen fotoğrafın kotrastını  non lineer olarak azaltır.
"""
def non_linear_lower_cont():
    global photoProc, labelProc
    matrix = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(matrix.shape[2]):
                matrix[i, j, k] = min(255, (matrix[i, j, k] / 255.0) ** 0.33) * 255.0
    show_processed_image(matrix)

"""
Yüklenen fotoğrafın kotrastını  non lineer olarak artırır.
"""
def non_linear_raise_cont():
    global photoProc, labelProc
    matrix = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(matrix.shape[2]):
                matrix[i, j, k] = min(255, (matrix[i, j, k] / 255.0) ** 2) * 255.0
    show_processed_image(matrix)

"""
Resim yükleme
"""
def load_image():
    global image
    try:
        imagePath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
        if len(imagePath) != 0:
            image = cv2.imread(imagePath)
            image = cv2.resize(image, (300, 300))  # Yüklenen resmi 300x300 olacak şekilde resize et.
            lblPath.config(text=imagePath)
            #print_image_pixel(image) Ödev-2
            show_image(image)
    except Exception as e:
        lblPath.config(text="Resim yükleme hatası!")
        print(f"Hata: {e}")

"""
Component yerleşimeri
"""
btnLoadImage = tk.Button(form, text="Resim Yükle", command=load_image)
btnLoadImage.grid(row=0, column=0, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

lblPath = tk.Label(form, text="-")
lblPath.grid(row=1, column=0, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=8)

btnInvert = tk.Button(form, text="Invert", command=invert)
btnInvert.grid(row=0, column=1, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

btnDarken = tk.Button(form, text="Darken", command=darken)
btnDarken.grid(row=0, column=2, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

btnDarken = tk.Button(form, text="Lighten", command=lighten)
btnDarken.grid(row=0, column=3, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

btnLower = tk.Button(form, text="Lower Cont.", command=lower_cont)
btnLower.grid(row=0, column=4, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

btnRaise = tk.Button(form, text="Raise Cont.", command=raise_cont)
btnRaise.grid(row=0, column=5, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

btnNonLower = tk.Button(form, text="Non Linear\n Lower Cont.", command=non_linear_lower_cont)
btnNonLower.grid(row=0, column=6, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

btnNonRaise = tk.Button(form, text="Non Linear\n Raise Cont.", command=non_linear_raise_cont)
btnNonRaise.grid(row=0, column=7, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

tk.mainloop()
