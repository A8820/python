rus_equal = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_list_equal = []
with open('Task 5.4_SAV.txt', 'r') as file_obj:
    content = file_obj.read().split('\n')
    for i in file_obj:
        i = i.split(' ', 1)
        new_list_equal.append(rus_equal[i[0]] + '  ' + i[1])
    print(new_list_equal)

