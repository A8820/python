
initial_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
"""Исходный список"""

final_list = [el for num, el in enumerate(initial_list) if initial_list[num - 1] < initial_list[num]]
"""Новый список записывает каждый предыдущий элемент исходного списка, 
если последующий элемент последовательности больше"""

print(f'Исходный список: {initial_list}')
print(f'Новый список: {final_list}')
