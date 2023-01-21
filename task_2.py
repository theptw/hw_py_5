# Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом
from random import randint

pole1 = [1,2,3]
pole2 = [4,5,6]
pole3 = [7,8,9]
poles = [pole1,pole2,pole3]
corners = [1,3,7,9]

def pole_print(list1, list2, list3):
    print('|', end='')
    print(*pole1, end='')
    print('|')

    print('|', end='')
    print(*pole2, end='')
    print('|')

    print('|', end='')
    print(*pole3, end='')
    print('|')

pole_print(pole1, pole2, pole3)

def win_condition_x(list1, list2, list3): # выиграли ли крестики
    if list1[0] == 'X' and list2[1] == 'X' and list3[2] == 'X':
        return True
    elif list1[1] == 'X' and list2[1] == 'X' and list3[1] == 'X':
        return True
    elif list1[2] == 'X' and list2[1] == 'X' and list3[0] == 'X':
        return True
    elif list1[0] == 'X' and list1[1] == 'X' and list1[2] == 'X':
        return True
    elif list2[0] == 'X' and list2[1] == 'X' and list2[2] == 'X':
        return True
    elif list3[0] == 'X' and list3[1] == 'X' and list3[2] == 'X':
        return True
    elif list1[0] == 'X' and list2[0] == 'X' and list3[0] == 'X':
        return True
    elif list1[1] == 'X' and list2[1] == 'X' and list3[1] == 'X':
        return True
    elif list1[2] == 'X' and list2[2] == 'X' and list3[2] == 'X':
        return True
    else:
        return False

def win_condition_o(list1, list2, list3): # выиграли ли нолики
    if list1[0] == 'O' and list2[1] == 'O' and list3[2] == 'O':
        return True
    elif list1[1] == 'O' and list2[1] == 'O' and list3[1] == 'O':
        return True
    elif list1[2] == 'O' and list2[1] == 'O' and list3[0] == 'O':
        return True
    elif list1[0] == 'O' and list1[1] == 'O' and list1[2] == 'O':
        return True
    elif list2[0] == 'O' and list2[1] == 'O' and list2[2] == 'O':
        return True
    elif list3[0] == 'O' and list3[1] == 'O' and list3[2] == 'O':
        return True
    elif list1[0] == 'O' and list2[0] == 'O' and list3[0] == 'O':
        return True
    elif list1[1] == 'O' and list2[1] == 'O' and list3[1] == 'O':
        return True
    elif list1[2] == 'O' and list2[2] == 'O' and list3[2] == 'O':
        return True
    else:
        return False

def check_if_busy(list1, list2, list3, num): # проверка не занято ли поле
    global turn
    if num == 1 and (list1[0] == 'X' or list1[0] == 'O'):
        num = int(input('Это поле занято, введите другое: '))
        turn = num
    elif num == 2 and (list1[1] == 'X' or list1[1] == 'O'):
        num = int(input('Это поле занято, введите другое: '))
        turn = num
    elif num == 3 and (list1[2] == 'X' or list1[2] == 'O'):
        num = int(input('Это поле занято, введите другое: '))
        turn = num
    elif num == 4 and (list2[0] == 'X' or list2[0] == 'O'):
        num = int(input('Это поле занято, введите другое: '))
        turn = num
    elif num == 5 and (list2[1] == 'X' or list2[1] == 'O'):
        num = int(input('Это поле занято, введите другое: '))
        turn = num
    elif num == 6 and (list2[2] == 'X' or list2[2] == 'O'):
        num = int(input('Это поле занято, введите другое: '))
        turn = num
    elif num == 7 and (list3[0] == 'X' or list3[0] == 'O'):
        num = int(input('Это поле занято, введите другое: '))
        turn = num
    elif num == 8 and (list3[1] == 'X' or list3[1] == 'O'):
        num = int(input('Это поле занято, введите другое: '))
        turn = num
    elif num == 9 and (list3[2] == 'X' or list3[2] == 'O'):
        num = int(input('Это поле занято, введите другое: '))
        turn = num

def bot(list, turn_count, corners):
    if turn_count == 1: # елси второй ход - ход в центр или угол
        if poles[1][1] == 5:
            return poles[1][1]
        else:
            return corners[randint(0,3)]

#bot win condition   
    for j in range(len(poles)): # два o по горизонтали
        if poles[j].count('O') == 2:
            for i in range(3):
                if type(poles[j][i]) == int:
                    return poles[j][i]
                    
    search_vertical_win = [] #если два o по вертикали
    for j in range(3):
        for i in range(3):
            search_vertical_win.append(poles[i][j])
        if search_vertical_win.count('O') == 2:
            for b in range(len(search_vertical_win)):
                if type(search_vertical_win[b]) == int:
                    return search_vertical_win[b]
        else: search_vertical_win.clear()

    search_diagonal_win = [] # диагональ слева на право
    j = 0
    for i in range(3):
        search_diagonal_win.append(poles[j][i])
        j += 1
    if search_diagonal_win.count('O') == 2:
        for b in range(len(search_diagonal_win)):
            if type(search_diagonal_win[b]) == int:
                return search_diagonal_win[b]
    
    diagonal_left_win = [] # диагональ на лево
    j = 0
    for i in range(2,-1,-1):
        diagonal_left_win.append(poles[j][i])
        j += 1
    if diagonal_left_win.count('O') == 2:
        for b in range(len(diagonal_left_win)):
            if type(diagonal_left_win[b]) == int:
                return diagonal_left_win[b]
            
#bot not to lose
    for j in range(len(poles)): # два х по горизонтали
        if poles[j].count('X') == 2:
            for i in range(3):
                if type(poles[j][i]) == int:
                    return poles[j][i]
                    
    search_vertical = [] #если два х по вертикали
    for j in range(3):
        for i in range(3):
            search_vertical.append(poles[i][j])
        if search_vertical.count('X') == 2:
            for b in range(len(search_vertical)):
                if type(search_vertical[b]) == int:
                    return search_vertical[b]
        else: search_vertical.clear()

    search_diagonal = [] # диагональ слева на право
    j = 0
    for i in range(3):
        search_diagonal.append(poles[j][i])
        j += 1
    if search_diagonal.count('X') == 2:
        for b in range(len(search_diagonal)):
            if type(search_diagonal[b]) == int:
                return search_diagonal[b]
    
    search_diagonal_left = [] # диагональ на лево
    j = 0
    for i in range(0,3,-1):
        search_diagonal_left.append(poles[j][i])
        j += 1
    if search_diagonal_left.count('X') == 2:
        for b in range(len(search_diagonal_left)):
            if type(search_diagonal_left[b]) == int:
                return search_diagonal_left[b]

    # если след. ходом нельзя выиграть или не дать выиграть оппоненту:
    for j in range(3):
        if poles[j].count('O') == 1 and poles[j].count('X') == 0: # приоритет на линии без крестиков
            for i in range(3):
                if poles[j][i] != 'O':
                    return poles[j][i]
    for j in range(3): #если нет - любой ход(ничья)
        for i in range(3):
            if type(poles[j][i]) == int:
                return poles[j][i]
            
                
    



which_turn = 0
for j in range(9):
    if which_turn % 2 == 1:
        turn = bot(poles, which_turn, corners)
        print('Бот сходил, поле выглядит так: ')
    else:
        turn = int(input('Ходят крестики, введите номер клетки: '))
    check_if_busy(pole1,pole2,pole3,turn)
    
    for i in range(3):
        if turn == pole1[i]:
            if which_turn % 2 == 0:
                pole1[i] = 'X'
            else: pole1[i] = 'O'

    for i in range(3):
        if turn == pole2[i]:
            if which_turn % 2 == 0:
                pole2[i] = 'X'
            else: pole2[i] = 'O'

    for i in range(3):
        if turn == pole3[i]:
            if which_turn % 2 == 0:
                pole3[i] = 'X'
            else: pole3[i] = 'O'

    pole_print(pole1, pole2, pole3)
    print('_________')
    

    if win_condition_x(pole1,pole2,pole3) == True:
        print('Крестики выиграли!')
        break
    elif win_condition_o(pole1,pole2,pole3) == True:
        print('Нолики выиграли!')
        break
    elif which_turn == 8:
        print('Ничья!')
        break  

    which_turn += 1
    




