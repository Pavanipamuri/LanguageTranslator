from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

languages = {
    'en': 'English',
    'hi': 'Hindi',
    'te': 'Telugu',
    'ta': 'Tamil',
    'fr': 'French',
    'es': 'Spanish',
    'de': 'German',
    'ja': 'Japanese',
    'ko': 'Korean',
    'zh-CN': 'Chinese'
}

@app.route('/', methods=['GET', 'POST'])
def home():

    translated_text = ""

    if request.method == 'POST':

        text = request.form['text']
        source = request.form['source']
        target = request.form['target']

        translated_text = GoogleTranslator(
            source=source,
            target=target
        ).translate(text)

    return render_template(
        'index.html',
        translated_text=translated_text,
        languages=languages
    )

if __name__ == '__main__':
    app.run(debug=True)