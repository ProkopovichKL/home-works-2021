﻿1. Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел, 
отсортированных по возрастанию, которая этот список “сворачивает”.

get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
get_ranges([4,7,10])  -> "4, 7, 10"
get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"


x = [0, 2, 4, 4, 4, 7, 7, 8, 10, 10, 10, 12, 14, 16, 18, 18, 18, 19, 20, 21, 22]
x = sorted(set(x)) # Получаем на вход отсортированный список неповторяющихся целых чисел

def new_list(x):
    y = [x[0]]     # Создаём список со значением первого элемента "x"    
    z = []         # А этот список нам нужен для "складывания" вложенных списков из цикла № 1
    for i in range(1, len(x)):      # Это цикл № 1 - он наполняет "z" вложенными списками
        if x[i] - x[i-1] == 1:
            y.append(x[i])
        else:
            z.append(list(y))
            y.clear()
            y.append(x[i])
        if i == (len(x)-1) and x[i] - x[i-1] == 1:
            y.append(x[i])
            z.append(list(y))
        elif i == (len(x)-1) and x[i] - x[i-1] != 1:
            z.append(list(y))
    for n in range(len(z)):         # Это цикл № 2 - он проходит по вложенным спискам "z" для печати.
        if len(z[n]) == 1:
            print(f"'{z[n][0]}'", end = ' ')
        else:
            print(f"'{z[n][0]}-{z[n][-1]}'", end = ' ')
        
new_list(x)