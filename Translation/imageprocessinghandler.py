from PIL import Image
import pytesseract

class ImageProcessingHandler:

    def GetTextFromImage(self, image, language):
        text = './media/' + image
        return pytesseract.image_to_string(Image.open(text), lang=language)