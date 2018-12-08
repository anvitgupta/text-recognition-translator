import unittest
from translatehandler import TranslationHandler
from imageprocessinghandler import ImageProcessingHandler

class TranslationTests(unittest.TestCase):

    def testgettextfromimage(self):
        imageprocessor = ImageProcessingHandler()
        text = imageprocessor.GetTextFromImage("spanish.png", "spa")
        self.assertEqual(text, "Yo vivo en Nashville")

    def testdetectenglish(self):    
        translator = TranslationHandler()
        language = translator.DetectLanguage("this is english").lang
        self.assertEqual(language, 'en')
    
    def testdetectspanish(self):
        translator = TranslationHandler()
        language = translator.DetectLanguage('おはようございます').lang
        self.assertEqual(language, 'ja')

    def testtranslatetext(self):
        translator = TranslationHandler()
        text = translator.TranslateText('esto es espanol').text 
        self.assertEqual(text, 'this is Spanish')

if __name__=='__main__':
    unittest.main()