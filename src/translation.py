import os

import requests
from dotenv import load_dotenv

load_dotenv('conf/.env')

API_KEY = os.getenv('DEEPL_API_KEY')


def translate_to_german(sentence):
    base_url = "https://api-free.deepl.com/v2/translate"
    headers = {
        "Authorization": f"DeepL-Auth-Key {API_KEY}"
    }
    data = {
        "text": sentence,
        "target_lang": "DE",
        "source_lang": "EN"
    }
    response = requests.post(base_url, headers=headers, data=data)
    translation = response.json()['translations'][0]['text']
    return translation

# translated_sentence = translate_to_german("Couple nights ago, I could've sworn I saw a picture move.")
# print(translated_sentence)

# todo linguee for word translation
