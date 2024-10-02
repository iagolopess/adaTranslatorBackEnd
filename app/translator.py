import requests
import json
from googletrans import Translator

def translate_text(text_to_translate, target_lang):
    json_data = ""
    url = "https://trans.zillyhuhn.com/translate"  

    data = {
        "q": text_to_translate,
        "source": "auto",
        "target": target_lang,
        "format": "text",
        "alternatives": 3,
        "api_key": ""  
    }

    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, headers=headers, json=data, timeout=1.5)  

        
        if response.status_code == 200:
            data = response.json()  
            json_data = json.dumps(data)  
            translated_obj = json.loads(json_data)
            return translated_obj.get("translatedText")  
        else:
            print("Falha na requisição do primeiro tradutor, usando alternativo")
            return alternative_translator(text_to_translate, target_lang).text
    except requests.exceptions.Timeout:
        print("Falha na requisição do primeiro tradutor, usando alternativo")
        return alternative_translator(text_to_translate, target_lang).text
    except requests.exceptions.RequestException as e:
       
        print(f"Ocorreu um erro na requisição: {e}")
        return None


def alternative_translator(original_text, lang_target):
    translator = Translator()
    translated = translator.translate(original_text, dest=lang_target)
    return translated

