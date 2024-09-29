import requests
import json
from googletrans import Translator

def translate_text(text_to_translate, target_lang):
    json_data = ""
    # Defina a URL da API
    url = "https://trans.zillyhuhn.com/translate"

# Defina os dados do corpo da requisição
    data = {
        "q": text_to_translate,
        "source": "auto",
        "target": target_lang,
        "format": "text",
        "alternatives": 3,
        "api_key": ""
    } 

# Defina os cabeçalhos
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, json=data)  # Passe o 'json=data' aqui

# Verifique o status da resposta
    if response.status_code == 200:
        data = response.json()  # Parse o JSON da resposta
        print(data)
        json_data = json.dumps(data)  # Converta o dicionário para uma string JSON, se necessário
        translated_obj = json.loads(json_data)
        return translated_obj.get("translatedText")
    elif(response.status_code != 200 or json_data == "null"):
        translator = Translator()
        translated = translator.translate(text_to_translate, dest=target_lang)
        return translated.text
    else: 
        return response.status_code

    
