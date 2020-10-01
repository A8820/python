
from functools import reduce

def initial_func(element, element_):
    return element * element_

print(f'Четные числа последовательности: {[el for el in range(99, 1001) if el % 2 == 0]}')

print(f'Произведение элементов последовательности: '
          f'{reduce(initial_func, [el for el in range(99, 1001) if el % 2 == 0])}')