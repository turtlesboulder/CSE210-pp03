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
        self.displayed_word = self._word.get_word_display() 
        self.game_output()
        self.game_loop()

    def end_game(self):
        pass

    def game_loop(self):
        while not self._word.is_done() and self._num_strings > 0:
            self.game_input()
            self.game_update()
            self.game_output()
        print(f"The word was: {self._my_word}")
    
    def game_input(self):
        self.letter = self._console.get_input()

    def game_update(self):
        if not self._word.get_if_letter_in_word(self.letter):
            self._num_strings -= 1
        self.displayed_word = self._word.get_word_display()

    def game_output(self):
        self._console.print_strings(self._num_strings)
        print(f"\n{self.displayed_word}")

