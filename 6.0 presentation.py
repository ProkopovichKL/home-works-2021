import bl

def show_result():
    x = input('\nEnter your expression: ')
    bl.result(x)

def show_query(message):
    return input(format_message(message, ':\n'))

def format_message(message, end):
    return message + end

def main_flow():
    while True:
        choise = show_query('\nChouse the operation (calculate, exit)')
        if choise == 'calculate':
            show_result()
            continue
        elif choise == 'exit':
            break
        else:
            print('Incorrect input, try again.')
            continue

if __name__ == '__main__':
    main_flow()