import tkinter as tk
import cv2
from tkinter import filedialog
from PIL import Image, ImageTk


class ImageProcessor:
    def __init__(self):
        self.image = None

    def show_image(self):
        if self.image is not None:
            normalImage = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            photo = ImageTk.PhotoImage(image=Image.fromarray(normalImage))
            label = tk.Label(self.form, image=photo)
            label.grid(row=2, column=0, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=8)
            label.image = photo

    def load_image(self, path):
        try:
            self.image = cv2.imread(path)
            self.image = cv2.resize(self.image, (300, 300))
            return self.image
        except Exception as e:
            print(f"Hata: {e}")

    def invert(self):
        if self.image is not None:
            matrix = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            for i in range(matrix.shape[0]):
                for j in range(matrix.shape[1]):
                    for k in range(matrix.shape[2]):
                        matrix[i, j, k] = max(0, 255 - matrix[i, j, k])
            return Image.fromarray(matrix)
        return None

    def darken(self):
        if self.image is not None:
            matrix = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            for i in range(matrix.shape[0]):
                for j in range(matrix.shape[1]):
                    for k in range(matrix.shape[2]):
                        matrix[i, j, k] = max(0, matrix[i, j, k] - 128)
            return Image.fromarray(matrix)
        return None

    def lighten(self):
        if self.image is not None:
            matrix = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            for i in range(matrix.shape[0]):
                for j in range(matrix.shape[1]):
                    for k in range(matrix.shape[2]):
                        matrix[i, j, k] = min(255, matrix[i, j, k] + 128)
            return Image.fromarray(matrix)
        return None

    def lower_contrast(self):
        if self.image is not None:
            matrix = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            for i in range(matrix.shape[0]):
                for j in range(matrix.shape[1]):
                    for k in range(matrix.shape[2]):
                        matrix[i, j, k] = round(matrix[i, j, k] / 2)
            return Image.fromarray(matrix)
        return None

    def raise_contrast(self):
        if self.image is not None:
            matrix = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            for i in range(matrix.shape[0]):
                for j in range(matrix.shape[1]):
                    for k in range(matrix.shape[2]):
                        matrix[i, j, k] = min(255, matrix[i, j, k] * 2)
            return Image.fromarray(matrix)
        return None

    def non_linear_lower_contrast(self):
        if self.image is not None:
            matrix = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            for i in range(matrix.shape[0]):
                for j in range(matrix.shape[1]):
                    for k in range(matrix.shape[2]):
                        matrix[i, j, k] = min(255, (matrix[i, j, k] / 255.0) ** 0.33) * 255.0
            return Image.fromarray(matrix)
        return None

    def non_linear_raise_contrast(self):
        if self.image is not None:
            matrix = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            for i in range(matrix.shape[0]):
                for j in range(matrix.shape[1]):
                    for k in range(matrix.shape[2]):
                        matrix[i, j, k] = min(255, (matrix[i, j, k] / 255.0) ** 2) * 255.0
            return Image.fromarray(matrix)
        return None