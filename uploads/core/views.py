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

        translated_text = imageprocessor.GetTextFromImage(myfile.name)

        sound_file = soundconverter.ConvertToSound(translated_text)
        timestamp = str(time.strftime("%Y%m%d-%H%M%S"))
        sound_file.save('./media/' + timestamp + '.mp3')
        sound_file_url = fs.url(timestamp + ".mp3")

        return render(request, 'core/simple_upload.html', {
            'translated_text': translated_text,
            'sound_file_url' : sound_file_url,
        })
    return render(request, 'core/simple_upload.html')
