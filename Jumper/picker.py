import random
import json

class Picker:
    def __init__(self):
        with open("jumper/words.json", "r+") as word_list:
            words_string = word_list.read()
            words = json.loads(words_string)
        self.words_array = words["array"]

    def get_word(self):
        word_choice = random.randint(0,len(self.words_array)-1)
        new_word = self.words_array[word_choice]
        return new_word