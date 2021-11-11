from console import Console
from director import Director
from picker import Picker
from word import Word

def main():
    my_console = Console()
    my_picker = Picker()
    my_word = Word("apple")

    for _ in range(3):
        word_display = my_word.get_word_display()
        print(word_display)
        print(my_word.get_if_letter_in_word("a"))




if __name__ == "__main__":
    main()