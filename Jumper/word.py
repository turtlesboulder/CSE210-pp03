class Word:
    def __init__(self, new_word):
        self._word = new_word
        self._word_display = ""
        self._make_word_display()

    def _make_word_display(self):
        new_word = ""
        for _ in self._word:
            if _ != " ":
                new_word += f"_ "
            else:
                new_word += "  "

        self._word_display = new_word

    def get_if_letter_in_word(self, guess):
        self._reveal_letter(guess)
        return guess in self._word

    def _reveal_letter(self, guess):
        for i in range(len(self._word)):
            if self._word[i] == guess: #and self._word_display[i*2] != guess:
                self._word_display = self._word_display[:i*2] + guess + self._word_display[i*2+1:]

    def get_word_display(self):
        return self._word_display

    def is_done(self):
        return "_" not in self._word_display