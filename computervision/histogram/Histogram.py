"""
 @author Seyit Ahmet ÖZDEMİR
 @project pytonworkspace Histogram
 @date 06 Kas 2023
 <p>
 @description: Bir resmin kırmızı, yeşil, mavi ve gri tonlamalarının histogramlarını gösteren kod örneği
"""
"""
 @author Seyit Ahmet ÖZDEMİR
 @project pytonworkspace ImageProcess
 @date 28 Eki 2023
 <p>
 @description: Görüntü İşleme Uygulaması
"""

import tkinter as tk
import cv2
from tkinter import filedialog
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pyplot as plt

form = tk.Tk()
form.geometry("700x500")
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
labelDesc = None

"""
Yüklenen fotoğrafı gösterir
"""
def show_image(image):
    global photo, label
    normalImage = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    photo = ImageTk.PhotoImage(image=Image.fromarray(normalImage))
    label = tk.Label(form, image=photo)
    label.grid(row=3, column=0, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=4)

"""
İşlenmiş fotoğrafı gösterir
"""
def show_processed_image(matrix):
    global photoProc, labelProc
    photoProc = ImageTk.PhotoImage(image=Image.fromarray(matrix))
    labelProc = tk.Label(form, image=photoProc)
    labelProc.grid(row=3, column=4, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=4)


"""
Yapılan işlemi yazdırır.
"""


def show_process_description(text):
    global labelDesc
    labelDesc = tk.Label(form, text=text)
    labelDesc.grid(row=2, column=7, padx=5, pady=5, sticky="w", rowspan=1, columnspan=2)
    pass

def red_histogram():
    global image
    hist_r = cv2.calcHist([image], [0], None, [256], [0, 256])
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.plot(hist_r, color='red')
    ax.set_title('Red Histogram')
    ax.set_xlabel('Pixel Value')
    ax.set_ylabel('Frequency')

    canvas = FigureCanvasTkAgg(fig, master=tk)
    canvas.draw()
    canvas.get_tk_widget().pack(padx=10, pady=10)


def green_histogram():
    global image
    hist_g = cv2.calcHist([image], [1], None, [256], [0, 256])
    plt.plot(hist_g, color='green')
    plt.title('Green Histogram')
    plt.show()

def blue_histogram():
    global image
    hist_b = cv2.calcHist([image], [2], None, [256], [0, 256])
    plt.plot(hist_b, color='blue')
    plt.title('Blue Histogram')
    plt.show()

def gray_histogram():
    global image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist_gray = cv2.calcHist([gray], [0], None, [256], [0, 256])
    plt.plot(hist_gray, color='black')
    plt.title('Grayscale Histogram')
    plt.show()

"""
Resim yükleme
"""
def load_image():
    global image
    try:
        imagePath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
        if len(imagePath) != 0:
            image = cv2.imread(imagePath)
            image = cv2.resize(image, (300, 300))  # Yüklenen resmi 300x300 olacak şekilde resize et.
            lblPath.config(text=imagePath)
            # print_image_pixel(image) Ödev-2
            show_image(image)
    except Exception as e:
        lblPath.config(text="Resim yükleme hatası!")
        print(f"Hata: {e}")


"""
Component yerleşimeri
"""
btnLoadImage = tk.Button(form, text="Resim Yükle", command=load_image)
btnLoadImage.grid(row=0, column=0, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

btnRedHist = tk.Button(form, text="Red Histogram", command=red_histogram)
btnRedHist.grid(row=0, column=1, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

btnGreenHist = tk.Button(form, text="Green Histogram", command=green_histogram)
btnGreenHist.grid(row=0, column=2, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

btnBlueHist = tk.Button(form, text="Blue Histogram", command=blue_histogram)
btnBlueHist.grid(row=0, column=3, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

btnGrayHist = tk.Button(form, text="Grayscale Histogram", command=gray_histogram)
btnGrayHist.grid(row=0, column=4, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

lblPath = tk.Label(form, text="-")
lblPath.grid(row=1, column=0, padx=5, pady=5, sticky="w", rowspan=1, columnspan=8)

lblInfo = tk.Label(form, text="Seyit Ahmet ÖZDEMİR\n202285151045")
lblInfo.grid(row=2, column=0, padx=5, pady=5, sticky="w", rowspan=1, columnspan=6)

tk.mainloop()
