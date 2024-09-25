from flask import Flask, request, jsonify
from flask_cors import CORS
from googletrans import Translator

app = Flask(__name__)
CORS(app, resources={r"/translate": {"origins": "*"}})

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.json  # Recebe dados do frontend (em JSON)
    text_to_translate = data['text']  # Texto a ser traduzido
    target_lang = data.get('lang', 'pt')  # Idioma de destino, padrão 'en' (inglês)
    
    translator = Translator()
    translated = translator.translate(text_to_translate, dest=target_lang)

    return jsonify({'translated_text': translated.text})  # Retorna a tradução como JSON

if __name__ == '__main__':
    app.run(debug=True)