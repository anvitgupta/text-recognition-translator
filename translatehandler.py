from googletrans import Translator

class TranslatorHandler()
    
    def __init__(self):
        self.translator = Translator()

    def DetectLanguage(detectedtext):
        return self.translator.detect(detectedtext)
    
    def TranslateText(detectedtext):
        return self.translator.translate(detectedtext)