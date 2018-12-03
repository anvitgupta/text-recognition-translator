import time
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from Translation.imageprocessinghandler import ImageProcessingHandler
from Translation.conversionhandler import ConversionHandler
from Translation.translatehandler import TranslationHandler
from uploads.core.models import Document
from uploads.core.forms import DocumentForm

def home(request):
    documents = Document.objects.all()
    return render(request, 'core/home.html', { 'documents': documents })

def simple_upload(request):
    
    imageprocessor = ImageProcessingHandler()
    soundconverter = ConversionHandler()
    translator = TranslationHandler()

    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        filename = get_file(request, myfile)
        sound_file = process_text(imageprocessor, translator, soundconverter, request, myfile) 

        sound_file_url = save_sound_file()
        
        return render(request, 'core/simple_upload.html', {
            'translated_text': translated_text,
            'sound_file_url' : sound_file_url,
        })

    return render(request, 'core/simple_upload.html')

def get_file(request, myfile):
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    return filename

def process_text(imageprocessor, translator, soundconverter, request, myfile):
    text_from_image = imageprocessor.GetTextFromImage(myfile.name, request.POST['language'])
    translated_text = translator.TranslateText(text_from_image).text
    sound_file = soundconverter.ConvertToSound(translated_text)
    return sound_file

def save_sound_file():
    timestamp = str(time.strftime("%Y%m%d-%H%M%S"))
    try:
        sound_file.save('./media/' + timestamp + '.mp3')
    except:
        print('ignore this error')

    return FileSystemStorage().url(timestamp + '.mp3')
        