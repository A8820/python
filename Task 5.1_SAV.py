
my_text_file = open('Task 5.1_SAV.txt', 'w')
line = input('Введите текст: \n')
while line:
    my_text_file.writelines(line)
    line = input('Введите текст либо пустую строку для завершения: \n')
    if not line:
        break

my_text_file.close()
my_text_file = open('Task 5.1_SAV.txt', 'r')
content = my_text_file.readlines()
print(content)
my_text_file.close()
