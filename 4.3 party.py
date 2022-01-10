2. Написать программу для вычисления суммы долга при расчёте в ресторане. 
Например, счёт в 150$ делится на троих, участник №1 внёс 100$, двое остальных (№2 и №3) - 15$ и 35$ соответственно. 
Программа должна оповестить пользователя о том, что участник №2 должен участнику №1 ещё 35$, а участник №3 - ещё 15$.

Пользователь вводит сумму счёта, количество участников, их суммы. [100,15,35]


# Округление использовал только для вывода данных через "print".
# В строке 7 от суммы каждого участника отнял средний чек: с отрицательными значениями - должники, с положительными - кредиторы.   
check_sum = float(input('Введите сумму счёта - '))
num_clients = int(input('Введите количество участников банкета - '))
medium_chk = float(check_sum/num_clients)  
clients_check = input('Введите взносы участников через запятую без пробелов - ').split(',')
cl_chk = [(float(i) - medium_chk) for i in clients_check]  # Это генератор списка должников и кредиторов. 

def dept_control(cl_chk, num_clients):
    for i in range(num_clients):
        if cl_chk[i] < 0:
            if abs(cl_chk[i]) <= max(cl_chk):
                print(f'участник {(i)+1} должен участнику {cl_chk.index(max(cl_chk)) + 1} {round(abs(cl_chk[i]), 2)}')
                cl_chk[cl_chk.index(max(cl_chk))] += cl_chk[i]
                cl_chk[i] += abs(cl_chk[i])
            elif abs(cl_chk[i]) > max(cl_chk):
                while abs(cl_chk[i]) != 0:
                    if max(cl_chk) < 0.01:
                        break
                    print(f'участник {(i)+1} должен участнику {cl_chk.index(max(cl_chk)) + 1} {round(max(cl_chk), 2)}')
                    cl_chk[i] += max(cl_chk)
                    cl_chk[cl_chk.index(max(cl_chk))] = 0

dept_control(cl_chk, num_clients)