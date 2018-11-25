from PIL import Image
import pytesseract

# text = pytesseract.image_to_string(Image.open('test.png'))

# print (text)


class ImageProcessingHandler:

    def GetTextFromImage(self, image):
        text = './media/' + image
        return pytesseract.image_to_string(Image.open(text))