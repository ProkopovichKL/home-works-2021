import data as d
# Первая функция для расчетов соседних целых цифровых элементов списка, если они не разделены скобками.
# Она применяется во второй функции со строки № 43.
def calculate(new_n):
    for i in range(len(new_n)):
        if new_n[i] == '+' and new_n[i+1] not in d.arifmetics and new_n[i-1] not in d.arifmetics:
            z = new_n[i-1] + new_n[i+1]
            new_n[i-1], new_n[i], new_n[i+1] = '', '', z
        elif new_n[i] == '-' and new_n[i+1] not in d.arifmetics and new_n[i-1] not in d.arifmetics:
            z = new_n[i-1] - new_n[i+1]
            new_n[i-1], new_n[i], new_n[i+1] = '', '', z
        elif new_n[i] == '*' and new_n[i+1] not in d.arifmetics and new_n[i-1] not in d.arifmetics:
            z = new_n[i-1] * new_n[i+1]
            new_n[i-1], new_n[i], new_n[i+1] = '', '', z
        elif new_n[i] == '/' and new_n[i+1] not in d.arifmetics and new_n[i-1] not in d.arifmetics:
            z = new_n[i-1] / new_n[i+1]
            new_n[i-1], new_n[i], new_n[i+1] = '', '', z
    while '' in new_n:         # Этот цикл "подчищает" список лишних элементов после завершения "for".
            new_n.remove('')
    return new_n     

# Вторая функция получает строку из арифметических выражений. 
def result(x):
    for i in x:    # Встроенная валидация.
        if i in d.numbers or i in d.arifmetics:
            continue
        else:
            print('Invalid enter. Try again.')
            return False
    new_n = [] 
    for index, value in enumerate(x): # Этот цикл создает список, в котором "строчные цифры"
        if value in d.numbers:        # замещаются цифрами с типом "int".
            new_n.append(int(value))   
        elif value in d.arifmetics:
            new_n.append(value)
    for i in range(len(new_n)-1): # Этот цикл "склеивает разбитые списком" цифры. 
        if new_n[i] not in d.arifmetics and new_n[i+1] not in d.arifmetics:
            z = int(str(new_n[i]) + str(new_n[i+1]))
            new_n[i], new_n[i+1] = '', z
    while '' in new_n:         # Этот цикл "подчищает" список лишних элементов после завершения "for".
            new_n.remove('')        
    while len(new_n) != 1:  # Этот цикл гоняет по кругу список, убирая скобки после расчетов  
        calculate(new_n)    # первой функции, тем самым давая первой функции проводить 
        while '(' in new_n: # операции с соседними элементами, пока список не составит 1 элемент.
            new_n.remove('(')
        calculate(new_n)
        while ')' in new_n:
            new_n.remove(')')
    print('Your result:', new_n[0])