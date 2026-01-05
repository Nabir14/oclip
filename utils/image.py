from PIL import ImageGrab
from .extra import Extra

class Image:
    img = None

    @staticmethod
    def take_screenshot(pos1, pos2):
        Image.img = ImageGrab.grab(bbox=Extra.to_bbox_coords(pos1, pos2))
        return Image.img

    @staticmethod
    def preview_screenshot():
        if Image.img:
            Image.img.show()
        else:
            print("Image Is Empty")