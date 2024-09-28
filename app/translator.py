from googletrans import Translator

def translate_text(text_to_translate, target_lang):
    lang_to_translate = target_lang
    if(target_lang == "autoDetect"):
        lang_to_translate = translator.detect(target_lang)

    translator = Translator()
    translated = translator.translate(text_to_translate, dest=lang_to_translate)
    return translated.text
