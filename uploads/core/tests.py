from views import home, simple_upload, get_file, process_text, save_sound_file
from django.utils import unittest
from django.test.client import RequestFactory

class SimpleTest(unittest.TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_home(self):
        request = self.factory.get('/home')

        response = my_view(request)
        self.assertEqual(response.status_code, 200)
    
    def test_simpleupload(self):
        response = self.factory.post('/uploads/simple', 'uploads\Images\spanish.png')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type('text/html'))

    def test_getfile(self):
        request = 



