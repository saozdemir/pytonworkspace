import tkinter as tk

import cv2

import ImageProcessor
from tkinter import filedialog
from PIL import Image, ImageTk

class GuiImageProcessor:
    def run(self):
        self.form.mainloop()

    def __init__(self):
        self.form = tk.Tk()
        self.form.geometry("700x700")
        self.form.title("Görüntü İşleme")

        self.processor = ImageProcessor()
        self.run(self)

    def load_image(self):
        try:
            image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
            if len(image_path) != 0:
                self.processor.load_image(image_path)
                self.show_image(self.processor.image)
        except Exception as e:
            print(f"Hata: {e}")

    def show_image(self, image):
        normal_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        photo = ImageTk.PhotoImage(image=Image.fromarray(normal_image))
        label = tk.Label(self.form, image=photo)
        label.grid(row=2, column=0, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=4)
        self.form.mainloop()

