from director import Director
from word import Word
from picker import Picker
def main():
    number = 6
    picker = Picker()
    word = Word(picker.get_word())
    # word.get_string(number)
    director = Director()
    director.start_game()
    director.game_loop()
    director.end_game()


if __name__ == "__main__":
    main()