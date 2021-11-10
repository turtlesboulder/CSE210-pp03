class Console:
    def __init__(self):
       pass

        
    def console_print(self, my_string:str):
        print(my_string)

    def get_input(self):
        self.guess = input("Guess a letter: ")
        return self.guess
    
    def print_strings(self, number):
        self.line = open(f"{number}-string-jumper.txt")
        for i in self.line:
            print(i, end="")


    

    
