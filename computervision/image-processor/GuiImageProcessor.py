import tkinter as tk
import ImageProcessor
from tkinter import filedialog
from PIL import Image, ImageTk

class GuiImageProcessor:
    def __init__(self, image_processor):
        self.processor = image_processor

        self.form = tk.Tk()
        self.form.geometry("900x700")
        self.form.title("Görüntü İşleme")

        self.btnLoadImage = tk.Button(self.form, text="Resim Yükle", command=self.load_image)
        self.btnLoadImage.grid(row=0, column=0, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

        self.lblPath = tk.Label(self.form, text="-")
        self.lblPath.grid(row=1, column=0, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=8)

        self.btnInvert = tk.Button(self.form, text="Invert", command=self.invert)
        self.btnInvert.grid(row=0, column=1, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

        self.btnDarken = tk.Button(self.form, text="Darken", command=self.darken)
        self.btnDarken.grid(row=0, column=2, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

        self.btnLighten = tk.Button(self.form, text="Lighten", command=self.lighten)
        self.btnLighten.grid(row=0, column=3, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

        self.btnLowerCont = tk.Button(self.form, text="Lower Cont.", command=self.lower_contrast)
        self.btnLowerCont.grid(row=0, column=4, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

        self.btnRaiseCont = tk.Button(self.form, text="Raise Cont.", command=self.raise_contrast)
        self.btnRaiseCont.grid(row=0, column=5, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

        self.btnNonLinearLowerCont = tk.Button(self.form, text="Non Linear\n Lower Cont.",
                                               command=self.non_linear_lower_contrast)
        self.btnNonLinearLowerCont.grid(row=0, column=6, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

        self.btnNonLinearRaiseCont = tk.Button(self.form, text="Non Linear\n Raise Cont.",
                                               command=self.non_linear_raise_contrast)
        self.btnNonLinearRaiseCont.grid(row=0, column=7, padx=5, pady=5, sticky="nsew", rowspan=1, columnspan=1)

    def show_image(self):
        pass
    def load_image(self):
        try:
            image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
            if len(image_path) != 0:
                success = self.processor.load_image(image_path)
                if success:
                    self.lblPath.config(text=image_path)
                    self.processor.show_image()
        except Exception as e:
            self.lblPath.config(text="Resim yükleme hatası!")
            print(f"Hata: {e}")

    def invert(self):
        processed_image = self.processor.invert()
        self.show_processed_image(processed_image)

    def darken(self):
        processed_image = self.processor.darken()
        self.show_processed_image(processed_image)

    def lighten(self):
        processed_image = self.processor.lighten()
        self.show_processed_image(processed_image)

    def lower_contrast(self):
        processed_image = self.processor.lower_contrast()
        self.show_processed_image(processed_image)

    def raise_contrast(self):
        processed_image = self.processor.raise_contrast()
        self.show_processed_image(processed_image)

    def non_linear_lower_contrast(self):
        processed_image = self.processor.non_linear_lower_contrast()
        self.show_processed_image(processed_image)

    def non_linear_raise_contrast(self):
        processed_image = self.processor.non_linear_raise_contrast()
        self.show_processed_image(processed_image)

    def show_processed_image(self, processed_image):
        if processed_image is not None:
            photo = ImageTk.PhotoImage(processed_image)
            label = tk.Label(self.form, image=photo)
            label.grid(row=2, column=0, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan=8)
            label.image = photo
    def run(self):
        self.form.mainloop()

# if __name__ == "__main__":
#     processor = ImageProcessor()
#     gui = GuiImageProcessor(processor)
#     gui.run()