class Console:
    def __init__(self):

       self._has_guessed = False
       

    def instructions(self):
        self.instructions_text = open("instructions.txt")
        for i in self.instructions:
            print(i, end="")

    def get_input(self, number):
        
        self._guess = str(input("Guess a letter [a-z]: "))
        return self._guess
    
    def print_strings(self, number_string):
        self._line = open(f"{number_string}-string-jumper.txt")
        for i in self._line:
            print(i, end="")


    

    
