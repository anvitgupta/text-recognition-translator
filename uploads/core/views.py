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
        soundfilename = sound_file.save(path)
        sound_file_url = fs.url(soundfilename)

        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url,
            'translated_text': translated_text,
            'sound_file_url' : sound_file_url
        })
    return render(request, 'core/simple_upload.html')

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })
