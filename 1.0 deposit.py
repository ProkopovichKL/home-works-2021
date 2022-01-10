'''Я, если честно, немного в замешательстве. Ниже первый вариант расчёта без использования decimal.
C 14-ой строки у меня вариант с использованием decimal. И результат один и тот же.
Хотя мне казалось, что decimal изменит результаты вывода (не могу понять, где ошибка).
И последнее: в Excel я произвел расчёты и там результат оказался - 42 143,47 (меньше на 0,16).
В обоих вариантах я использовал формулу сложных процентов.'''

# Это первый вариант Version 1 - совсем упрощённый.
deposit, procent, mounth = 20000, 15, 60
prmounth = (procent/12)
new_deposit = deposit * (1 + (prmounth/100))**mounth
print('Your new deposit is (Version 1) - ', round(new_deposit, 2))

# А это второй вариант - Version 2.
from decimal import *
deposit = 20000.00
deposit = Decimal(deposit)
procent = 15.00
procent = Decimal(procent)
mounth = 60
mounth = int(mounth)
prmounth = Decimal(procent/12)
new_deposit = deposit * (1 + (prmounth/100))**mounth
print('Your new deposit is (Version 2) - ', round(new_deposit, 2))