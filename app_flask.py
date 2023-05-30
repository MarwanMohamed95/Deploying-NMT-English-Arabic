import numpy as np
from flask import Flask, request, render_template
import tensorflow as tf
import tensorflow_text as tf_text
import warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)

languageDetector = tf.saved_model.load('languageDetector')
EngAra = tf.saved_model.load('English_Arabic_Translator')
AraEng = tf.saved_model.load('Arabic_English_Translator')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detect_language', methods=['POST'])
def detect_language():
    input_text = request.form['text']
    language = languageDetector(input_text).numpy()[0].decode()
    return render_template('index.html', language=language)

@app.route('/translate_text', methods=['POST'])
def translate_text():
    input_text = request.form['text']
    language = languageDetector(input_text).numpy()[0].decode()

    if language == "English":
        translated_text = EngAra(input_text).numpy().decode()
    
    elif language == "Arabic":
        translated_text = AraEng(input_text).numpy().decode()

    else:
        translated_text =  "Language is not supported"

    return render_template('index.html', language = language, translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True)
