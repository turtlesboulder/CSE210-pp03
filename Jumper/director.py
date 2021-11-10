from console import Console
from word import Word
from picker import Picker
class Director:
    def __init__(self):
        self.console = Console()
        self.picker = Picker()
        self.my_word = picker.get_word()
        self.word = Word(my_word)
        self.num_strings = 6

    def start_game(self):
        self.console.instructions()
        # console.parachute()
        displayed_word = self.word.get_word_display()

    def end_game(self):
        pass

    def game_loop(self):
        pass