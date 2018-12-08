import unittest
from translatehandler import TranslationHandler
from imageprocessinghandler import ImageProcessingHandler

class TranslationTests(unittest.TestCase):

    def testdetectenglish(self):    
        translator = TranslationHandler()
        self.assertEqual(translator.DetectLanguage("this is english").lang, 'en')
    
    def testdetectspanish(self):
        translator = TranslationHandler()
        self.assertEqual(translator.DetectLanguage('esto es espanol').lang, 'es')

    def testtranslatetext(self):
        translator = TranslationHandler()
        self.assertEqual(translator.TranslateText('esto es espanol').text, 'this is Spanish')

if __name__=='__main__':
    unittest.main()