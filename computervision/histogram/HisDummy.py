import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


def calculate_red_histogram(image):
    b, g, r = cv2.split(image)
    hist_r = cv2.calcHist([r], [0], None, [256], [0, 256])
    return hist_r


def show_red_histogram():
    global image
    hist_r = calculate_red_histogram(image)

    fig = Figure(figsize=(5, 4))
    ax = fig.add_subplot(111)
    ax.plot(hist_r, color='red')
    ax.set_title('Red Histogram')

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


def load_image():
    global image, photo, label
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
    if file_path:
        image = cv2.imread(file_path)
        image = cv2.resize(image, (300, 300))
        show_image(image)


def show_image(image):
    global photo, label
    normal_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    photo = ImageTk.PhotoImage(image=Image.fromarray(normal_image))
    label = tk.Label(window, image=photo)
    label.grid(row=3, column=0, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=1)


window = tk.Tk()
window.geometry("400x400")
window.title("Red Histogram")

photo = None
label = None
image = None

btnLoadImage = tk.Button(window, text="Resim Yükle", command=load_image)
btnLoadImage.grid(row=0, column=0, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

btnShowRedHistogram = tk.Button(window, text="Red Histogramı Göster", command=show_red_histogram)
btnShowRedHistogram.grid(row=1, column=0, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

window.mainloop()
