import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2021-08-16',
    authenticator=authenticator
)
language_translator.set_service_url(url)


def englishToFrench(english_text):
    """
    Translation text from English to French
    """

    french_translation = language_translator.translate(
        text = english_text,
        model_id='en-fr'
    ).get_result()
    french_text = french_translation.get("translations")[0].get("translation")
    return french_text


def frenchToEnglish(french_text):
    """
    Translation text from French to English
    """

    english_translation = language_translator.translate(
        text = french_text,
        model_id='fr-en'
    ).get_result()
    english_text = english_translation.get("translations")[0].get("translation")
    return english_text