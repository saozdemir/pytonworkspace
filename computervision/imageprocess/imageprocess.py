"""
#author: saozdemir
#description: Görüntü İşleme Uygulaması

"""

import tkinter as tk
from tkinter import filedialog

import cv2

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
def load_image():
    try:
        imagePath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
        if len(imagePath) != 0:
            image = cv2.imread(imagePath)
            image = cv2.resize(image, (300, 300))  # Yüklenen resmi 300x300 olacak şekilde resize et.
            lblPath.config(text=imagePath)
            print_image_pixel(image)
    except Exception as e:
        lblPath.config(text="Resim yükleme hatası!")
        print(f"Hata: {e}")


btnLoadImage = tk.Button(form, text="Resim Yükle", command=load_image)
btnLoadImage.grid(row=0, column=0, padx=10, pady=10)
# btnLoadImage.pack(anchor="nw", padx=5, pady=5)

lblPath = tk.Label(form, text="-")
lblPath.grid(row=0, column=1, padx=10, pady=10)

tk.mainloop()
