class TicTacToe:

    def __init__(self):
        self.__board = [['-' for j in range(3)] for i in range(3)]    # Создаем доску для игры 3 на 3 
                                                                      # из вложенных списков.
    def player_choice(self, line, column, player):  # Присваиваем значение "player" ("X" или "O") для ячейки доски
        self.__board[line][column] = player         # после вовода игроком номеров строки и столбца.

    def is_player_win(self, player):  # Решил выбрать прямое решение (перечисление выигрышных комбинаций), так как  
        win = True                    # не ставил задачу по масштабированию игры (так меньше строк код, как ни странно).
        if ((self.__board[0][0] == player and self.__board[0][1] == player and self.__board[0][2] == player) or
            (self.__board[1][0] == player and self.__board[1][1] == player and self.__board[1][2] == player) or 
            (self.__board[2][0] == player and self.__board[2][1] == player and self.__board[2][2] == player) or
            (self.__board[0][0] == player and self.__board[1][0] == player and self.__board[2][0] == player) or
            (self.__board[0][1] == player and self.__board[1][1] == player and self.__board[2][1] == player) or
            (self.__board[0][2] == player and self.__board[1][2] == player and self.__board[2][2] == player) or
            (self.__board[0][0] == player and self.__board[1][1] == player and self.__board[2][2] == player) or
            (self.__board[0][2] == player and self.__board[1][1] == player and self.__board[2][0] == player)):
            return win         # Если применять изменяемые параметр для настроки доски (6*6, 9*9 и т.д.), то проверку  
                               # выигрышей однозначно лучше проводить циклами for (подсмотрено в интернете). 
    def is_board_filled(self):
        for line in self.__board:    # Проверяем заполненность доски: если не осталось "пустых" ячеек - игра
            for i in line:           # завершается ничьей. 
                if i == '-':
                    return False
        return True

    def change_player(self, player):
        if player == 'X':            # После первой итерации цикла меням игрока присваиванием нового значения.
            return 'O'               # Если верить Википедии, первыми всегда начинают "Х".
        else:
            return 'X'

    def show_board(self):
        for line in self.__board:    # На каждой итерации цикла "рисуем" текущее состояние доски. 
            for i in line:
                print(i, end=' ')
            print()

    def get_and_check_item(self):    # Этот блок отрабатывает ошибки ввода: 1. число вне диапазона от 1 до 3, 
        while True:                  # 2. если выбирают уже заполненную ячейку, 3. ввод любого "не числа". 
            try:
                self.__line = int(input("Enter line number (only 1, 2 or 3): "))
                self.__column = int(input("Enter column number (only 1, 2 or 3): "))
                if self.__line not in range(1,4) or self.__column not in range(1,4):
                    raise IndexError
                elif self.__board[self.__line - 1][self.__column - 1] != '-':
                    raise SyntaxError
            except IndexError:
                print("\nYou can't write any integers except 1, 2 or 3. Try again!")
            except ValueError:
                print("\nYou can't write any symbols except integers 1, 2 or 3. Try again!")
            except SyntaxError:
                print("\nYou cannot overwrite the previous selection (yours or your opponent's). Try again!")
            else:
                return self.__line, self.__column  

    def start_game(self):         # Блок с игрой 
        player = 'X'
        count = 1
        while True:
            print(f"\nStep № {count} is for the player who enters '{player}'")
            self.show_board()    # Показываем доску.
            while True:
                self.get_and_check_item() # Просим ввести игрока очередной ход и проверяем.  
                if self.__board[self.__line - 1][self.__column - 1] == '-': # Если он не "перетирает" предыдущий/свой
                    break                                                   # выбор игрока - выходим и присваиваем
            self.player_choice(self.__line - 1, self.__column - 1, player)  # ячейке его "Х" или "О". 
            if self.is_player_win(player):    # Проверяем на выигрыш.
                print(f"\nThe player who entered '{player}' wins the game on the step № {count}!")
                break
            elif self.is_board_filled():      # Проверяем на заполненность на случай ничейного результата. 
                print("\nGame over - it's a draw!")
                break
            player = self.change_player(player)  # "Меняем игрока" после завершения итерации.
            count += 1
        self.show_board()

ttt = TicTacToe()
ttt.start_game()