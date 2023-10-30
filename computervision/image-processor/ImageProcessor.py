import cv2

class ImageProcessor:
    def __init__(self):
        self.image = None

    def load_image(self, image_path):
        self.image = cv2.imread(image_path)
        self.image = cv2.resize(self.image, (300, 300))

    def invert(self):
        # İşlemler burada yapılacak
        pass

    def darken(self):
        # İşlemler burada yapılacak
        pass

    def lighten(self):
        # İşlemler burada yapılacak
        pass

    def lower_contrast(self):
        # İşlemler burada yapılacak
        pass

    def raise_contrast(self):
        # İşlemler burada yapılacak
        pass

    def non_linear_lower_contrast(self):
        # İşlemler burada yapılacak
        pass

    def non_linear_raise_contrast(self):
        # İşlemler burada yapılacak
        pass