import csv
import os
import boto3
import six
from google.cloud import translate_v2 as translate

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ""

def translate_text(target, text):
    translate_client = translate.Client()
    
    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    lines = text.splitlines()
    for line in lines:
        result = translate_client.translate(line, target_language=target)
        print(u"Translation: {}".format(result["translatedText"]))

testStr = """

"""
if __name__ == '__main__':
    translate_text("en", testStr)
