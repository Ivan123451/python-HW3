# Первая задача:
# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению
from random import randint
n = int(input("длина списка: "))
list = []

for i in range(0, n):
    list.append(randint(0, 100))

print(list)

x = int(input("введите искомое число х: "))
sum = 0
if x in list:
    for i in range(0, n):
        if list[i] == x:
            sum += 1
    print(f"число {x} встерчается {sum} раза")

else:
    for i in range(0, 100):
        for j in range(0, n):
            if (list[j] + i == x) or (list[j] - i == x):
                y = list[j]
                print(f"максимально близкое к {x} по значению -  {y}")
                break
        if (list[j] + i == x) or (list[j] - i == x):
            break


