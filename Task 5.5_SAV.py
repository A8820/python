
def count_function():
    try:
        with open('Task 5.5_SAV.txt', 'w') as file_obj:
            line = input('Введите цифры через пробел: \n')
            file_obj.writelines(line)
            my_number = line.split()
            print(sum(map(int, my_number)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Ошибка ввода данных')
count_function()