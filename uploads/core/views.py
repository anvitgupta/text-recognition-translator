import time
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from Translation.imageprocessinghandler import ImageProcessingHandler
from Translation.conversionhandler import ConversionHandler
from uploads.core.models import Document
from uploads.core.forms import DocumentForm

def home(request):
    documents = Document.objects.all()
    return render(request, 'core/home.html', { 'documents': documents })

def simple_upload(request):
    imageprocessor = ImageProcessingHandler()
    soundconverter = ConversionHandler()

    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        time.sleep(3)
        translated_text = imageprocessor.GetTextFromImage(myfile.name)

        sound_file = soundconverter.ConvertToSound(translated_text)
        path = './media/sound.mp3'
        sound_file.save(path)
        sound_file_url = fs.url("sound.mp3")

        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url,
            'translated_text': translated_text,
            'sound_file_url' : sound_file_url,
            'file_name' : filename
        })
    return render(request, 'core/simple_upload.html')
