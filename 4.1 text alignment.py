with open('text.txt', 'r') as f:
    l = [line.strip() for line in f] # Создаём список.
l = str(l)
# Убираем лишние элементы текста. 
l = l.replace("['", '') 
l = l.replace("', '", ' ')
l = l.replace("']", '')

# Эта группа кода создана для генерации списка "new" без выравнивания,
# так как сделать всё в одном списке мне не вышло.
new = []
x = int(input('Ведите максимальное количество символов в строке (не менее 36) - '))
while True:        # Проверка на введение верной комбинации чисел.
    if x > 35:
        break
    elif x <= 35:
        x = int(input('Вы ввели менее 36, попробуйте снова - '))
y = x # Это надо для итераций цикла на первоначално заданное "х-значение"
b = 0
for i in range(len(l)): # Формируем список с выравниванием по левому краю. 
    c = b + y # Это счётчик для того, чтобы следующая строка была не больше "x". 
    if i < c:
        new.append(l[i])
    elif i == c:
        new.append(l[i])
        for n in range(y):
            a = - n - 1
            if new[a] == ' ':
                new[a] = '\n'
                b = ''.join(new).rindex('\n') + 1
                break
    x += y

news = new # Создаём на всякий случай дублирующий список.
           # С ним и дальше работаем. 
new_n = [] # Вычленяем все вхождения '\n' в списке для последующего цикла выравнивания.
for index, value in enumerate(news):
    if value == '\n':
        new_n.append(index)   

# Цикл по выравниванию текста. К сожалениею, функциями пока владею плохо - поэтому копипаст.
for m in range(len(new_n)):
    if new_n[m] < y:   # Это итерация для первого прохода цикла
        k = new_n[m]   # Она нужна для выравнивания первой строки при вводе любой цифры,
        while k < y:   # если длина строки меньше "x".
            for p in range(0, y):
                    if k >= y:
                        break
                    elif news[p] == ' ':
                        news[p] += ' '
                        k += 1
                    elif news[p] == '  ':
                        news[p] += ' '
                        k += 2
                    elif news[p] == '   ':
                        news[p] += ' '
                        k += 3
                    elif news[p] == '    ':
                        news[p] += ' '
                        k += 4
                    elif news[p] == '     ':
                        news[p] += ' '
                        k += 5
    if new_n[m] > y:                    # Не смог найти причины, по которой выравнивание не всегда происходит. 
        k = new_n[m] - new_n[m-1] - 1   # Одно понятно, чем больше "x", тем лучше результат.
        while k < y:                    # Проверял неоднократно - "х" = 95 красиво получается.
            s1 = new_n[m-1]
            s2 = new_n[m]
            for p in range(s1, s2):
                if k >= y:
                    break
                elif news[p] == ' ':
                    news[p] += ' '
                    k += 1
                elif news[p] == '  ':
                    news[p] += ' '
                    k += 2
                elif news[p] == '   ':
                    news[p] += ' '
                    k += 3
                elif news[p] == '    ':
                    news[p] += ' '
                    k += 4
                elif news[p] == '     ':
                    news[p] += ' '
                    k += 5      
news = ''.join(news)

with open("new_text.txt", 'w+', encoding = "utf-8") as file:
     file.writelines(news)
print('Создан новый файл с возможно неполным выравниванием - new_text.txt')