from translatehandler import TranslationHandler
from conversionhandler import ConversionHandler

translator = TranslationHandler()
converter = ConversionHandler()

while True:
    com = input("translate this: ")
    translation = translator.TranslateText(com)
    print(translation.text)
    converter.ConvertToSound(translation.text)