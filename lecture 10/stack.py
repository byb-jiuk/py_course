class Stack:
    def __init__(self):
        self.__stack = []
        print("stack sozdan yspeshno")
    def push(self, value):
        self.__stack.append(value)
        print(value, "dobavleno")
    def pop(self):
        try:
            print(self.__stack.pop(), "yspeshno delete.")
        except:
            print("stack yze pysto")
    def state(self):
        print("tekyshee sostoania")
        print(self.__stack)

        
class AddStackValues(Stack):
    def __init__(self):
        super().__init__()
        self.__summa = 0
    def push(self, value):
        super().push(value)
        self.__summa += value
    def get_summa(self):
        print(self.__summa)
