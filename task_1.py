# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит заданное количество конфет. 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются 
# сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллект'
from random import randint

total_sweets = int(input('Введите количество конфет: '))
names = []

for i in range(2):
    names.append(input(f'Введите имя {i+1}-го игрока: '))

turn = randint(0,1)
print(f"По результатам жеребьёвки ходит {names[turn]}")

take = 0
while total_sweets > 0:
    if turn == 0:
        take = int(input(f'Ходит {names[turn]}, сколько конфет Вы возьмёте?'))
        if take > 28:
            take = int(input('Нельзя брать больше 28 конфет, введите другое число: '))
        total_sweets -= take
        print(f'Осталось {total_sweets} конфет')
        turn = 1
    if total_sweets > 0 and turn == 1:
        take = int(input(f'Ходит {names[turn]}, сколько конфет Вы возьмёте?'))
        if take > 28:
            take = int(input('Нельзя брать больше 28 конфет, введите другое число: '))
        total_sweets -= take
        print(f'Осталось {total_sweets} конфет')
        turn = 0

if turn == 0:
    turn = 1
if turn == 1:
    turn = 0
print(f'{names[turn]} выйграл!')


    
