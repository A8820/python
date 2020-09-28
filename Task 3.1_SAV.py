
def div_function(*args):
    """Вводим функцию, принимающую два позиционных аргумента."""
    try:
        dividend = int(input("Введите делимое: "))
        divider = int(input("Введите делитель: "))
        res = dividend / divider
        """Вводим аргументы функции, принимающую два позиционных аргумента и переменную - результат их деления."""

    except ValueError:
        return "Ошибка ввода"
        """Исключаем ошибку ввода аргумента с неподдерживаемым значением."""
    except ZeroDivisionError:
        return "Деление на ноль"
    """Исключаем ошибку ввода делителя, равного нулю."""

    return res
    """Возвращаем результат деления аргументов функции."""

print(f'Частное: {div_function()}')
"""Выводим результат деления аргументов функций."""

