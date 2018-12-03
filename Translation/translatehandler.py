# Accesses the google translate api
from googletrans import Translator

class TranslationHandler:
    
    def __init__(self):
        self.translator = Translator()

    def DetectLanguage(self, detectedtext):
        return self.translator.detect(detectedtext)
    
    def TranslateText(self, detectedtext):
        return self.translator.translate(detectedtext)

    # print(translate.TranslateText("yo vivo en nashville"))