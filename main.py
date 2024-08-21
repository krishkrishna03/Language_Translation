from flask import Flask, render_template, request
from googletrans import Translator, LANGUAGES

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    translated_text = ""
    if request.method == 'POST':
        src_lang = request.form.get('src_lang')
        dest_lang = request.form.get('dest_lang')
        text = request.form.get('text')
        if text and src_lang and dest_lang:
            translator = Translator()
            translated = translator.translate(text=text, src=src_lang, dest=dest_lang)
            translated_text = translated.text
    languages = list(LANGUAGES.values())
    return render_template('index.html', translated_text=translated_text, languages=languages)

if __name__ == '__main__':
    app.run(debug=True)
