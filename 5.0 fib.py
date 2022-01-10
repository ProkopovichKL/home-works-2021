# 1. Дан список вида ['1', '11', '12', '22', '2', '13', '30', '33']. 
# Отсортировать его по возрастанию числовых значений, исключив те, квадраты которых являются чётными числами.
# Программа должна занимать одну строчку.
m = ['1', '11', '12', '22', '2', '13', '30', '33']
m = list(filter(lambda x : int(x) % 2 == 1, sorted(m)))
print(m)

# 2. Написать функцию для вычисления суммы всех элементов вложенных (любая глубина) списков.
# Пример списка (синтаксис Python): [1, 2, [2, 4, [[7, 8], 4, 6]]], сумма элементов - 34.
x = [1, 2, [2, 4, [[7, 8], 4, 6]]]
def list_ellem_sum(x:list) -> int:
    '''
    The function summarizes the elements of a list 
    (including nested lists) and print 'int' result.
    
    Params:
    x: list     
    
    Returns:
    int
    '''
    def ellem_sum(x): # Использовал вложенную функцию для встроенного вывода "print".
        if x == []:
            return x
        elif isinstance(x[0], list):
            return ellem_sum(x[0]) + ellem_sum(x[1:])
        else:
            return x[:1] + ellem_sum(x[1:])
    print("Сумма элементов списка -", sum(ellem_sum(x)))

list_ellem_sum(x)

# 3. Написать функцию для вычисления n первых чисел Фибоначчи.
# Примеры вызова: 
# fib(5) -> 0,1,1,2,3
# fib(10) -> 0,1,1,2,3,5,8,13,21,34  
def fibonacci_numbers():
    while True:
        n = input('Введите желаемое количество чисел Фибоначчи больше нуля - ')
        try:
            n = int(n)
            if n <= 0 or n > 40:
                raise ValueError
        except ValueError:
            print('Вы ввели нецелое число или символы (не цифры), или число меньше 1, или больше 40!')
            print('Не пытайтесь вводить число больше 40 - будет очень долгий расчёт!\n')
            continue
        else:
            break
    print(f'Первые {n} числа(ел) последовательности Фибоначчи - ', end = '')
    for i in range(n):  # Использовал цикл и вложенную функцию для встроенного вывода "print".
        def fib(i):
            if i <= 1:
                return i
            else:
                return fib(i-1) + fib(i-2)
        if i < (n-1):
            print(fib(i), end = ',')
        else:
            print(fib(i))

fibonacci_numbers()