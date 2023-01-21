# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит заданное количество конфет. 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются 
# сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллект'
from random import randint

total_sweets = int(input('Введите количество конфет: '))

turn = randint(0,1)
if turn == 0:
    print("По результатам жеребьёвки ходите Вы")
else:
    print('По результатам жеребьёвки ходит Бот')
take = 0
while total_sweets > 0:
    if turn == 0:
        take = int(input(f'Вы ходите, сколько конфет возьмёте?'))
        if take > 28 or take <= 0:
            take = int(input('Нельзя не брать конфеты или брать больше 28, введите другое число: '))
        total_sweets -= take
        print(f'Осталось {total_sweets} конфет')
        turn = 1
    if total_sweets > 0 and turn == 1:
        take = total_sweets % 29
        if take == 0:
            take = 1
        total_sweets -= take
        print(f'Bot взял {take} конфет, осталось {total_sweets}')
        turn = 0

if turn == 0:
    print('Вы проиграли :( ')
if turn == 1:
    print('Вы выйграли!')



    
