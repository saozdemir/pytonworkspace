import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk
import numpy as np

def load_image():
    global original_image

    # Kullanıcıya resim seçme penceresi açılır
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])

    if file_path:
        # Resmi yükle
        original_image = cv2.imread(file_path)
        original_image = cv2.resize(original_image, (300, 300))

        # Resmi Tkinter formatına dönüştür
        original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
        original_image = Image.fromarray(original_image)
        original_image = ImageTk.PhotoImage(original_image)

        # Resmi göster
        original_label.config(image=original_image)
        original_label.image = original_image

# Ana uygulama penceresini oluştur
root = tk.Tk()
root.title("Görüntü İşleme Uygulaması")

# Resim yükleme butonunu oluştur
load_button = tk.Button(root, text="Resim Yükle", command=load_image)
load_button.pack(pady=10)

# İlk görüntüyü gösteren etiket
original_label = tk.Label(root)
original_label.pack()

# İnvert edilmiş görüntüyü gösteren etiket
processed_label = tk.Label(root)
processed_label.pack()

# İşlem butonunu oluştur

# Uygulamayı başlat
root.mainloop()