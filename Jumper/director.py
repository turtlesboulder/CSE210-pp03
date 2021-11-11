from console import Console
from word import Word
from picker import Picker
class Director:
    def __init__(self):
        self._console = Console()
        self._picker = Picker()
        my_word = self._picker.get_word()
        self._word = Word(my_word)
        self._num_strings = 6

    def start_game(self):
        self._console.instructions()
        self._console.print_strings(self._num_strings)
        self.displayed_word = self._word.get_word_display()
        self.game_loop()

    def end_game(self):
        pass

    def game_loop(self):
        while not self._word.is_done():
            self.game_input()
            self.game_update()
            self.game_output()
        print("Done!")
    
    def game_input(self):
        self.letter = self._console.get_input()

    def game_update(self):
        if not self._word.get_if_letter_in_word(self.letter):
            self._num_strings -= 1
        self.displayed_word = self._word.get_word_display()

    def game_output(self):
        self._console.print_strings(self._num_strings)
        print(self.displayed_word)

