
class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input('Input any data and push Enter: '))
                self.my_list.append(val)
                print(f'Current list: {self.my_list} \n ')
            except:
                print(f"Unknown value")
                y_or_n = input(f'Try again? Y/N ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.my_input())
                elif y_or_n == 'N' or y_or_n == 'n':
                    return f'Game over, dude! Final list is: {self.my_list} \n '
                else:
                    return f'Game over, dude! final list is: {self.my_list} \n '

try_except = Error(1)
print(try_except.my_input())