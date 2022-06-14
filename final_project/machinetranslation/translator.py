'''Translator'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)
language_translator.set_service_url(url)

def English_to_French(english_text):
    """English to French"""
    frenchtrans = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    return frenchtrans["translations"][0]["translation"]

def French_to_English(french_text):
    """French to English"""
    englishtrans = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    return englishtrans["translations"][0]["translation"]

    
