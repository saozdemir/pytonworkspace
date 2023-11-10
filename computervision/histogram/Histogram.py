"""
 @author saozd
 @project pytonworkspace Histogram
 @date 06 Kas 2023
 <p>
 @description: Bir resmin kırmızı, yeşil, mavi ve gri tonlamalarının histogramlarını gösteren kod örneği
"""
import tkinter as tk
import cv2
from tkinter import filedialog
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pyplot as plt

form = tk.Tk()
form.geometry("1024x600")
form.title("Görüntü İşleme")

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
    label.grid(row=4, column=0, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=4)


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
    # Önceki histogramı temizle
    plt.clf()

    # Red Histogram
    red_hist = cv2.calcHist([image], [2], None, [256], [0, 256])

    plt.figure(figsize=(6, 4))

    # Histogramı göster
    plt.plot(red_hist, color='red')
    plt.title('Red Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.xlim([0, 255])
    # plt.yscale('log')

    # Histogramı Tkinter Label içinde göster
    fig = plt.gcf()
    canvas = FigureCanvasTkAgg(fig, master=form)
    canvas.draw()
    canvas.get_tk_widget().grid(row=4, column=4, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

def green_histogram():
    global image
    # Önceki histogramı temizle
    plt.clf()

    # Green Histogram
    green_hist = cv2.calcHist([image], [1], None, [256], [0, 256])
    plt.figure(figsize=(6, 4))
    # Histogramı göster
    plt.plot(green_hist, color='green')
    plt.title('Green Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.xlim([0, 255])
    # plt.yscale('log')

    # Histogramı Tkinter Label içinde göster
    fig = plt.gcf()
    canvas = FigureCanvasTkAgg(fig, master=form)
    canvas.draw()
    canvas.get_tk_widget().grid(row=4, column=4, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)
    #canvas.get_tk_widget().grid(row=4, column=0, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=4)


def blue_histogram():
    global image
    # Önceki histogramı temizle
    plt.clf()

    # Blue Histogram
    blue_hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    plt.figure(figsize=(6, 4))
    # Histogramı göster
    plt.plot(blue_hist, color='blue')
    plt.title('Blue Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.xlim([0, 255])
    # plt.yscale('log')

    # Histogramı Tkinter Label içinde göster
    fig = plt.gcf()
    canvas = FigureCanvasTkAgg(fig, master=form)
    canvas.draw()
    canvas.get_tk_widget().grid(row=4, column=4, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)
    #canvas.get_tk_widget().grid(row=4, column=0, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=4)


def grey_scale_histogram():
    global image
    # Önceki histogramı temizle
    plt.clf()

    # Görüntüyü gri tonlamalıya dönüştür
    grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Grey Scale Histogram
    grey_hist = cv2.calcHist([grey_image], [0], None, [256], [0, 256])
    plt.figure(figsize=(6, 4))
    # Histogramı göster
    plt.plot(grey_hist, color='grey')
    plt.title('Grey Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.xlim([0, 255])
    # plt.yscale('log')

    # Histogramı Tkinter Label içinde göster
    fig = plt.gcf()
    canvas = FigureCanvasTkAgg(fig, master=form)
    canvas.draw()
    canvas.get_tk_widget().grid(row=4, column=4, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

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

btnGreenHist = tk.Button(form, text="Gren Histogram", command=green_histogram)
btnGreenHist.grid(row=0, column=2, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

btnBlueHist = tk.Button(form, text="Blue Histogram", command=blue_histogram)
btnBlueHist.grid(row=1, column=1, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

btnGreyScaleHist = tk.Button(form, text="Gray Scale Histogram", command=grey_scale_histogram)
btnGreyScaleHist.grid(row=1, column=2, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

lblPath = tk.Label(form, text="-")
lblPath.grid(row=2, column=0, padx=5, pady=5, sticky="w", rowspan=1, columnspan=8)

lblInfo = tk.Label(form, text="Seyit Ahmet ÖZDEMİR\n202285151045")
lblInfo.grid(row=3, column=0, padx=5, pady=5, sticky="w", rowspan=1, columnspan=6)

tk.mainloop()

