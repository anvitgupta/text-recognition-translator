from translatehandler import TranslationHandler
from conversionhandler import ConversionHandler

translator = TranslationHandler()
converter = ConversionHandler()

while True:
    com = input("translate this: ")
    translation = translator.TranslateText(com)
    print(translator.DetectLanguage("test").lang)
    print(translator.TranslateText('esto es espanol'))
    converter.ConvertToSound(translation.text)