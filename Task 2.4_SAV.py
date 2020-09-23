
prnt_str = input("Введите строку: ")
word_list = []
num = 1
for el in range(prnt_str.count(' ') + 1):
    word_list = prnt_str.split()
    if len(str(word_list)) <= 10:
        print(f" {num} {word_list [el]}")
        num += 1
    else:
        print(f" {num} {word_list [el] [0:10]}")
        num += 1