import requests

# add credidentials
api_url = ''
api_key = ''

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

