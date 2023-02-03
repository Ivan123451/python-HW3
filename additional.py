
from random import randint

n = int(input('введите максимальную степень многочлена: '))

first_dict = dict()

for i in range(n + 1):
    first_dict[n-i] = randint(0, 100)
# print(first_dict)

mnogochlen = str()

for i in range(n+1):
    if n-i != 0:
        mnogochlen = mnogochlen + f' + {first_dict[n-i]}x^{n-i}'
    else:
        mnogochlen = mnogochlen + f' + {first_dict[n-i]}'

print(f'Первый многочлен {mnogochlen} = 0\n')

second_dict = dict()

for i in range(n + 1):
    second_dict[n-i] = randint(0, 100)
# print(second_dict)

mnogochlen2 = str()

for i in range(n+1):
    if n-i != 0:
        mnogochlen2= mnogochlen2 + f' + {second_dict[n-i]}x^{n-i}'
    else:
        mnogochlen2 = mnogochlen2 + f' + {second_dict[n-i]}'

print(f'Второй многочлен {mnogochlen2} = 0 \n ')

total_dict = dict()


for i in range(n+1):
    total_dict[n-i] = first_dict[n-i] + second_dict[n-i]

# print(total_dict)

mnogochlen_total = str()

for i in range(n+1):
    if n-i != 0:
        mnogochlen_total= mnogochlen_total + f' + {total_dict[n-i]}x^{n-i}'
    else:
        mnogochlen_total = mnogochlen_total + f' + {total_dict[n-i]}'

print(f'Сумма многочленов {mnogochlen_total} = 0 \n ')

