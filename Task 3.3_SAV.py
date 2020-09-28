
def sum_function(number1, number2, number3):
    """Вводим функцию трех позиционных аргументов."""

    number1 = int(input("Введите первое число: "))
    number2 = int(input("Введите второе число: "))
    number3 = int(input("Введите третье число: "))
    """Присваиваем аргументам значения вводимых пользователем чисел."""

    sum1 = number1 + number3
    sum2 = number2 + number3
    sum3 = number1 + number2
    """Присваиваем переменным комбинации сумм наибольших значений аргументов."""

    if number1 >= number3 and number2 >= number3:
        return sum3
    elif number1 > number2 and number1 < number3:
        return sum1
    else:
        return sum2
    """Возвращаем значения комбинаций сумм наибольших значений аргументов."""

print(f'Сумма наибольших чисел: {sum_function("","","")}')
"""Выводм сумму наибольших числе в результате итераций."""






