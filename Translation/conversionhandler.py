# Accesses the text conversion api
from gtts import gTTS
import time

class ConversionHandler:

    def ConvertToSound(self, translatedtext):
        return gTTS(translatedtext)