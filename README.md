# Text-Recognition-Translator

Text-Recognition-Translator is a cloud-enabled, Django powered image to translation to sound file converter.

### Tech

Text-Recognition uses a number of technologies and libraries:
* [Django] - python web framework
* [Bootstrap] - front-end design
* [gTTS] - creatse mp3 files
* [pytesseract] - text extraction
* [googletrans] - google translate
* [Amazon EC2] - deployment

### Installation

Text-Recognition requies:
Python 2.7
Django 2.1.4
Tesseract-ocr
gTTs
Ubuntu environment

### Running the project

1) git clone https://github.com/maxengel99/Text-Recognition-Translator.git 
2) cd into the repo
3) type out the following command: python3 manage.py runserver 0:8000
4) Navigate to port 8000 of your localhost
5) Upload a image file containing words

### Notes

We've currently turned off our AWS instance as we have a limited amount of credit. Please email anvit.gupta@vanderbilt.edu if you'd like to test it live.
