"""Определяем функцию трех вводимых пользователем параметров, с учетом цикла,
   возвращающего величину совокупного дохода до вычета налога либо ошибку ввода параметра"""

def income():

    try:
        volume = float(input("Выработка в часах: "))
        income_per_hour = float(input("Ставка, руб/час: "))
        bonus = float(input("Премия, руб: "))
        income = volume * income_per_hour + bonus
        print(f"Итого совокупный доход до вычета налога: {income}")

    except ValueError:
        print("Ошибка ввода параметра")

income()

