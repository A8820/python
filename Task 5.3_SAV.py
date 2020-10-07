
with open('Task 5.3_SAV.txt', 'r') as my_file:
    salary = []
    lower_salary = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           lower_salary.append(i[0])
        salary.append(i[1])
print(f'Оклад меньше 20.000 {lower_salary}, средний оклад {sum(map(int, salary)) / len(salary)}')