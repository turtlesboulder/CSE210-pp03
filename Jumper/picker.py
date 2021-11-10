import random
import json
import requests

class Picker:
    def __init__(self, new_word):
        with open('words.json', 'r+') as word_list:
            words_string = word_list.read()
        words = json.loads(words_string)
        words_array = words["array"]

    def get_word(self, words_array):
        word_choice = random.randint[1,len(words_array)]
        new_word = words_array[word_choice]
        return new_word