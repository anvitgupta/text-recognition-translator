from django.test import TestCase
from views import home, simple_upload, get_file, process_text, save_sound_file
from django.http import HttpRequest

request = HttpRequest()
request.method = 'POST'
request.META['language'] = 'spa'
requst.FILES[''] = 
