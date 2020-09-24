
data_count = int(input("Введите количество элементов списка: "))
data_box = []

i = 0
el = 0

while i < data_count:
          data_box.append(input("Введите следующее значение списка: "))
          i += 1

for element in range(int(len(data_box)/2)):
          data_box[el], data_box[el + 1] = data_box[el + 1], data_box[el]
          el += 2

print(data_box)
