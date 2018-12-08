from views import home, simple_upload, get_file, process_text, save_sound_file
from Translation.imageprocessinghandler import ImageProcessingHandler
from Translation.conversionhandler import ConversionHandler
from Translation.translatehandler import TranslationHandler
from django.utils import unittest
from django.test.client import RequestFactory
from django.http import HttpRequest

class SimpleTest(unittest.TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_home(self):
        request = self.factory.get('/home')

        response = my_view(request)
        self.assertEqual(response.status_code, 200)
    
    def test_simple_upload(self):
        response_spanish = self.factory.post('/uploads/simple', '\uploads\Images\spanish.png')
        self.assertEqual(response_spanish.status_code, 200)
        self.assertEqual(response_spanish.content_type('text/html'))
        
        response_arabic = self.factory.post('/uploads/simple', '\uploads\Images\Arabic.png')
        self.assertEqual(response_arabic.status_code, 200)
        self.assertEqual(response_arabic.content_type('text/html'))
        
        response_english = self.factory.post('/uploads/simple', '\uploads\Images\English.png')
        self.assertEqual(response_english.status_code, 200)
        self.assertEqual(response_english.content_type('text/html'))

        response_hindi = self.factory.post('/uploads/simple', '\uploads\Images\Hindi.png')
        self.assertEqual(response_hindi.status_code, 200)
        self.assertEqual(response_hindi.content_type('text/html'))

    def test_get_file(self):
        self.assertEqual(get_file('\uploads\Images\spanish.png'), 'spanish.png')
        self.assertEqual(get_file('\uploads\Images\Arabic.png'), 'Arabic.png')
        self.assertEqual(get_file('\uploads\Images\English.png'), 'English.png')
        self.assertEqual(get_file('\uploads\Images\Hindi.png'), 'Hindi.png')

    def test_process_text(self):
        imageprocessor = ImageProcessingHandler()
        soundconverter = ConversionHandler()
        translator = TranslationHandler()
        
        request_spanish = HttpRequest()
        request_spanish.method = 'POST'
        request_spanish.FILES['myfile'] = '\uploads\Images\spanish.png'
        
        request_english = HttpRequest()
        request_english.method = 'POST'
        request_english.FILES['myfile'] = '\uploads\Images\English.png'

        request_japenese = HttpRequest()
        request_japenese.method = 'POST'
        request_japenese.FILES['myfile'] = '\uploads\Images\Japanese.png'

        self.assertEqual(process_text((imageprocessor, translator, soundconverter, request_spanish, '\uploads\Images\spanish.png')), 'I live in Nashville')
        self.assertEqual(process_text((imageprocessor, translator, soundconverter, request_english, '\uploads\Images\English.png')), 'My name is Anvit Gupta. I am a computer science major at Vanderbilt University')
        self.assertEqual(process_text((imageprocessor, translator, soundconverter, request_japanese, '\uploads\Images\Japanese.png')), 'Hello, my name is It is Jon.')


if __name__=='__main__':
    unittest.main()

