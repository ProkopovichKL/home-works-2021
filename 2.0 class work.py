text = 'five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'
# Преобразуем в список.
text = text.split(' ')
print(text)
# Словарь для сравнения элементов - перемешан для того, чтобы последующий список
# с цифрами был не по порядку. 
numbers = {'eighteen':18, 'nineteen':19, 'twenty':20, 'five':5, 'six':6, 'eleven':11, 
'twelve':12, 'sixteen':16, 'thirteen':13,'seven':7, 'eight':8, 'nine':9, 'ten':10, 'fourteen':14, 
'fifteen':15, 'seventeen':17, 'one':1, 'two':2, 'three':3, 'four':4}
# Сравниваем словарь со списком
new_dict = {} # Создаём новый пустой словарь
for key, value in numbers.items():
    for i in text: # Сравниваем ключи со словаря 'numbers' с элементами списка 'text' 
        if i == key:
            new_dict[key] = value 
print(new_dict) #  Я не ожидал такого, но словарь получился без повторных элементов.
new_text = list(new_dict.values()) # Вычленяем список с "цифрами" из 'new_dict'. 
print(new_text)
new_text_sorted = sorted(new_text) # Сортируем список по функции 'sorted()'
print(new_text_sorted)

# Пытаемся вывести числа: сначала умножение, а потом сложение,
# и опять по кругу. Было сложно, но зато 'debag' освоил.  
for i in range(len(new_text_sorted)):
    i = i*2 # При втором прохождении цикла эта строка нам поможет. 
    a = new_text_sorted[i] * new_text_sorted[i+1]
    print(a, end = ' ')
# Строки 29-30 мне понадобились, чтобы избавиться от "IndexError: list index out of range"
    if i >= len(new_text_sorted)-2:   
        break
    else:
        b = new_text_sorted[i+1] + new_text_sorted[i+2]
    print(b, end = ' ')

# Это решения суммы нечётных элементов списка.
small = []  # Создаю новый список для заполнения нечетными числами.  
for i in range(len(new_text_sorted)):
    if i >= len(new_text_sorted): # Это наш прерыватель цикла.   
        break
    c = new_text_sorted[i]        # Присваиваем переменной числовое значение 'i'  
    if c % 2 != 0:
        small.append(new_text_sorted[i]) # Добавляем нечетный элемент в новый список
print(small)
print('\nСумма нечётных -', sum(small))





