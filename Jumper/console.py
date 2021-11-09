class Console:
    def __init__(self):
        self.file_name = "{}-string-jumper.txt"
        
    def console_print(self, my_string:str):
        print(my_string)

    def console_input(self):
        return input("")