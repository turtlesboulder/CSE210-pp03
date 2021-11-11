from console import Console
from word import Word
from picker import Picker
class Director:
    def __init__(self):
        self._console = Console()
        self._picker = Picker()
        self._my_word = self._picker.get_word()
        self._word = Word(self._my_word)
        self._num_strings = 6

    def start_game(self):
        self._console.instructions()
        # console.parachute()
        self.displayed_word = self._word.get_word_display()

    def end_game(self):
        pass

    def game_loop(self):
        self.game_input()
        self.game_update()
        self.game_output()
    
    def game_input(self):
        self.letter = self.console.get_input()
    def game_output(self):
        pass
    def game_update(self):
        pass