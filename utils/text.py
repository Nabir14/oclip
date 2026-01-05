import os
import pytesseract

class Text:
    pytesseract.pytesseract.tesseract_cmd = os.path.join(os.path.dirname(__file__), '..', 'tesseract', 'tesseract.exe')

    @staticmethod
    def extract(image):
        text = pytesseract.image_to_string(image)
        return text
