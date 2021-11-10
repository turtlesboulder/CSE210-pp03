from console import Console
from word import Word
from picker import Picker
class Director:
    def __init__(self):
        self._console = Console()
        self._picker = Picker()
        self._my_word = picker.get_word()
        self._word = Word(my_word)
        self._num_strings = 6

    def start_game(self):
        self._console.instructions()
        # console.parachute()
        displayed_word = self.word.get_word_display()

    def end_game(self):
        pass

    def game_loop(self):
        game_input()
        game_update()
        game_output()
    
    def game_input():
        self.letter = self.console.get_input()
    def game_output():
        pass
    def game_put():
        pass