
a = int(input("Введите пробег первого дня в км: "))
b = int(input("Введите цель в км: "))
start_day_result = 1
while a < b:
        a *= 1.1
        start_day_result += 1
print(f"Вы достигнете требуемых показателей на %.d день" % start_day_result)