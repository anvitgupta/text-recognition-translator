# Accesses the text conversion api
from gtts import gTTS
import time

class ConversionHandler:

    def ConvertToSound(self, translatedtext):
        tts = gTTS(translatedtext)
        timestr = time.strftime("%Y%m%d-%H%M%S")
        tts.save('./audio/' + timestr + '.mp3')

converter = ConversionHandler()
converter.ConvertToSound('hi there')