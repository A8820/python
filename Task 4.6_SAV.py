
from itertools import count

for el in count(3):
    if el > 10:
        break
    else:
        print(el)

from itertools import cycle

count = 0
for item in cycle(' Mes Que Un Club '):
    if count > 33:
        break
    else:
        print(item)
    count += 1