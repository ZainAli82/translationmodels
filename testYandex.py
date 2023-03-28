import requests

api_url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
api_key = 'trnsl.1.1.20230317T175938Z.2a7206f762410d4e.6903edb875127dc89a95f6822eed0ad9718ae5d5'

translation_direction = 'ur-en' 
text_format = 'plain' 
translation_options = '1' 

def translate_text():
    lines = text.splitlines()
    for line in lines:
        response = requests.get(api_url, params={
            'key': api_key,
            'text': line,
            'lang': translation_direction,
            'format': text_format,
            'options': translation_options
        })
        if response.status_code == 200:
            translation = response.json()['text'][0]
            print(translation)
        else:
            print('Error:', response.status_code)

text = """

"""
translate_text()

