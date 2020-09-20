
revenue = float(input("Введите выручку фирмы: "))
costs = float(input("Введите издержки фирмы: "))
if revenue > costs:
    print(f"Фирма работает с прибылью, чистая маржа составила: {((revenue - costs) / revenue)*100:.2f}%")
    employers = int(input("Введите количество сотрудников фирмы "))
    print(f"Прибыль в расчете на одного работника составила: {(revenue - costs) / employers:.2f}")
elif revenue == costs:
    print("Фирма безубыточна:)")
else:
    print("Фирма работает в убыток:(")