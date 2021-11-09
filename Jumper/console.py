class Console:
    def __init__(self):
        self.file_name = "{}-string-jumper.txt"

        
    def console_print(self, my_string:str):
        print(my_string)

    def get_input(self):
        guess = input("Guess a letter: ")
        return guess
    
    def print_strings(self, number):
        self.line = open(f"{number}-string-jumper.txt")
        for i in self.line:
            print(i, end="")


    

    