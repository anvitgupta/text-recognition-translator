from gtts import gTTS
tts = gTTS('hello')
tts.save('./audio/hello.mp3')