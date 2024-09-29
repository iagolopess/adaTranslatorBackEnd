from flask import request, jsonify

from .translator import translate_text

def configure_routes(app):
    @app.route('/translate', methods=['POST'])
    def translate():
        data = request.json
        text_to_translate = data['text']
        target_lang = data.get('lang', 'pt')
        
        translated_text = jsonify(translate_text(text_to_translate, target_lang))
        
        return translated_text
