import unittest
from Translation.translatehandler import TranslationHandler

class TranslationTests(unittest.TestCase):

    def test(self):    
        translator = TranslationHandler()
        self.assertEqual(translator.DetectLanguage("this is english"), 'en')

if __name__=='__main__':
    unittest.main()