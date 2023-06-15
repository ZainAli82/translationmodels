import requests, uuid, json

from decouple import Config

config = Config()
config.read_dotenv()

key = config.get('AZURE_KEY')
endpoint = config.get('AZURE_ENDPOINT')
location = config.get('AZURE_LOC')

def translate_text(text):
    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': 'ur',
        'to': ['en']
    }

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    lines = text.splitlines()
    for line in lines:
        body = [{
            'text': line
        }]
        request = requests.post(constructed_url, params=params, headers=headers, json=body)
        response = request.json()

    print(response[0]['translations'][0]['text'])

testText = """

"""

translate_text(testText)
