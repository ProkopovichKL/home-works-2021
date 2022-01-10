import random

def gen_password():
    '''
    This function is using for generate passwords.
    
    You can make cycle with 'gen_password()' to start generate passwords just like in this solution
    (all variables have already taken in the function):
        
        for n in gen_password():
            print(n)
            
    If you want to make a file with passwords you can use this solution:
    
        for n in gen_password():
            with open('password.txt', 'a') as doc:
                doc.write('\n' + n)
    '''
    basic_symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    spec_symbols = '!@#$%^&*()_-=|\/:;,.`~<>/*-+'   # Прописал все переменные внутри функции для возможности 
    combo_symbols = basic_symbols + spec_symbols    # импорта модуля в другие файлы. 
    password_length = int(input('Enter password length numerically: '))
    numbers_of_passwords = int(input('Enter the number of passwords needs: '))
    special_choice = input('If you need special characters in password, press "+", if not - press any other key: ')
    
    password = []
    x = 0
    while x < numbers_of_passwords:
        if special_choice == '+':
            for i in range(password_length):  # Применил двойной рандом для "улучшения рандомности)".
                password.append(random.choice(random.sample(combo_symbols, k=len(combo_symbols))))
            if spec_symbols not in password:  # Проверка на вхождение спец. символа: если нет - рандомному символу пароля присваивается рандомный спец. символ.  
                password[random.choice(range(password_length))] = random.choice(spec_symbols)
        elif special_choice != '+':
            for i in range(password_length):
                password.append(random.choice(random.sample(basic_symbols, k=len(basic_symbols))))
        yield ''.join(password)
        password = []
        x += 1

for n in gen_password():
    print(n)

for n in gen_password():
    with open('password.txt', 'a') as doc:
        doc.write('\n' + n)