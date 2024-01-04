"""
 @author Seyit Ahmet ÖZDEMİR
 @project pytonworkspace Blur
 @date 04 Oca 2024
 <p>
 @description: Mean, Medyan ve Gaussion Blur algoritmalarının uygulaması
"""
import tkinter as tk
import cv2
from tkinter import filedialog
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pyplot as plt

form = tk.Tk()
form.geometry("1024x600")
form.title("Görüntü İşleme - Blur")

photo = None
label = None
image = None
photoProc = None
labelProc = None
labelDesc = None

blur = None
blurPhoto = None
lblBlur= None

"""
Yüklenen fotoğrafı gösterir
"""
def show_image(image):
    global photo, label
    normalImage = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    photo = ImageTk.PhotoImage(image=Image.fromarray(normalImage))
    label = tk.Label(form, image=photo)
    label.grid(row=6, column=0, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=8)


"""
Yapılan işlemi yazdırır.
"""
def show_process_description(text):
    global labelDesc
    labelDesc = tk.Label(form, text=text)
    labelDesc.grid(row=2, column=7, padx=5, pady=5, sticky="w", rowspan=1, columnspan=2)

def mean_blur():
    global image, blur, blurPhoto
    blur = cv2.blur(image, (5, 5), (0, 0))  # 5x5 boyutunda kutu filtre uygulandı sol üst köşe merkez alındı
    blurPhoto = ImageTk.PhotoImage(image=Image.fromarray(blur))
    lblBlur = tk.Label(form, image=blurPhoto)
    lblBlur.grid(row=6, column=9, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=8)
    red_histogram()
    green_histogram()
    blue_histogram()
    gray_scale_histogram()

def medyan_blur():
    global image, blur, blurPhoto
    blur = cv2.medianBlur(image, 7)  # Kernel boyutu tek tam sayı olmalıdır.
    # Kernel boyutu ne kadar büyük olursa o kadar bulanık olur.
    # Medyan değeri bir veri kümesinin ortasında kalan değerdir. [1,2,3,4,5] de değer 3 olur.
    blurPhoto = ImageTk.PhotoImage(image=Image.fromarray(blur))
    lblBlur = tk.Label(form, image=blurPhoto)
    lblBlur.grid(row=6, column=9, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=8)
    red_histogram()
    green_histogram()
    blue_histogram()
    gray_scale_histogram()

def gaussion_blur():
    global image, blur, blurPhoto
    blur = cv2.GaussianBlur(image, (5, 5), 1, 0, 1)
    # (5,5) gaussian filtre boyutu
    # sigmax ve sigmay standart fağma değerleri
    # dst çıktı resminin depolanacağı NumPy dizisi
    blurPhoto = ImageTk.PhotoImage(image=Image.fromarray(blur))
    lblBlur = tk.Label(form, image=blurPhoto)
    lblBlur.grid(row=6, column=9, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=8)
    red_histogram()
    green_histogram()
    blue_histogram()
    gray_scale_histogram()

def red_histogram():
    global blur
    # Önceki histogramı temizle
    # plt.clf()

    # Red Histogram
    red_hist = cv2.calcHist([blur], [2], None, [256], [0, 256])

    plt.figure(figsize=(5, 3))

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
    canvas.get_tk_widget().grid(row=7, column=0, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=8)

def green_histogram():
    global blur
    # Önceki histogramı temizle
    # plt.clf()

    # Green Histogram
    green_hist = cv2.calcHist([blur], [1], None, [256], [0, 256])
    plt.figure(figsize=(5, 3))
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
    canvas.get_tk_widget().grid(row=7, column=9, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=8)


def blue_histogram():
    global blur
    # Önceki histogramı temizle
    # plt.clf()

    # Blue Histogram
    blue_hist = cv2.calcHist([blur], [0], None, [256], [0, 256])
    plt.figure(figsize=(5, 3))
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
    canvas.get_tk_widget().grid(row=8, column=0, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=8)


def gray_scale_histogram():
    global blur
    # Önceki histogramı temizle
    # plt.clf()

    # Görüntüyü gri tonlamalıya dönüştür
    grey_image = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)

    # Grey Scale Histogram
    grey_hist = cv2.calcHist([grey_image], [0], None, [256], [0, 256])
    plt.figure(figsize=(5, 3))
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
    canvas.get_tk_widget().grid(row=8, column=9, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=8)

"""
FileDialog ile resim seçimini alır
"""
def load_image():
    global image
    try:
        imagePath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
        if len(imagePath) != 0:
            image = cv2.imread(imagePath)
            # image = cv2.resize(image, (300, 300))  # Yüklenen resmi 300x300 olacak şekilde resize et.
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

btnMean = tk.Button(form, text="Mean Blur", command=mean_blur)
btnMean.grid(row=0, column=1, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

btnMedyan = tk.Button(form, text="Medyan Blur", command=medyan_blur)
btnMedyan.grid(row=0, column=2, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

btnGaussion = tk.Button(form, text="Gaussion Blur", command=gaussion_blur)
btnGaussion.grid(row=0, column=3, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

lblPath = tk.Label(form, text="-")
lblPath.grid(row=0, column=9, padx=5, pady=5, sticky="w", rowspan=1, columnspan=6)

lblInfo = tk.Label(form, text="Seyit Ahmet ÖZDEMİR\n202285151045")
lblInfo.grid(row=0, column=4, padx=5, pady=5, sticky="w", rowspan=1, columnspan=4)

tk.mainloop()