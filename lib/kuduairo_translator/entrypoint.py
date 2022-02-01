import pandas as pd
import unicodedata
import re

df = pd.read_csv("lib/kuduairo_translator/datasets/dataset.csv", nrows=261798)
dataset = dict(zip(df.portuguese, df.kuduairese))

def translate(sentence):
    words = re.compile("(\s|\!|\?|\,|\.|$)").split(sentence)
    translated_sentence = ""
    for word in words:
        current_word_is_uppercase = word.isupper()
        current_word_is_capitalized = not word.islower() and not word.isupper() and word.istitle()

        word = word.lower()
        word = strip_accents(word) if word != 'é' else word

        if word in dataset:
            word = dataset[word]
        
        if(current_word_is_uppercase):
            word = word.upper()
        elif(current_word_is_capitalized):
            word = word.capitalize()

        translated_sentence += word
    return translated_sentence


def strip_accents(text):
    text = unicodedata.normalize('NFD', text)\
           .encode('ascii', 'ignore')\
           .decode("utf-8")

    return str(text)
