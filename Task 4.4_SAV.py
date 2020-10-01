
initial_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
"""Исходный список"""

final_list = [el for el in initial_list if initial_list.count(el) < 2]
"""Новый список записывает каждый элемент исходного списка, не имеющий повторений"""

print(final_list)