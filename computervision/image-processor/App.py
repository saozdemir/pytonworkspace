from ImageProcessor import ImageProcessor
from GuiImageProcessor import GuiImageProcessor

if __name__ == "__main__":
    processor = ImageProcessor()
    gui = GuiImageProcessor(processor)
    gui.run()