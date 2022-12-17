# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока
#  делая ход друг после друга. Первый ход определяется жеребьёвкой. 
#  За один ход можно забрать не более чем 28 конфет. Все конфеты 
#  оппонента достаются сделавшему последний ход. Сколько конфет 
#  нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""


import random

def fankBot(N = 2021,p = 0,k = 28):
    N = N - p
    if (N % k) != 0:
        return N % k
    else:
        m = random.randint(1,k) 
        return m



def fankPlayer(p = 0,k = 28):
    while((p < 1) or (p > 28)):
        p = int(input(f'Введите число от 1 до {k} ->'))
        if((p < 1) or (p > 28)):
            print(f'Вы ввели число вне диапозона от 1 до {k},поробуйте снова')
        else: return p



userList = ['игрок','бот']
answer=input('Начинаем игру? напишите да или нет ->')
N = 2021
pip = random.randint(0,1)
print(f'Игру начинает {userList[pip]}')


while N != 0:
    if answer == 'да':
        if userList[pip] == 'игрок':
            answer1 = fankPlayer() 
            if N - answer1 == 0:
                print('Поздравляем игрок выиграл')
            answerBot = fankBot(N,answer1)
            N = N - answer1
            N = N - answerBot
            if N == 0:
                print('Поздравляем бот выиграл')
            else:
                print(f'Бот взял себе {answerBot} конфет,осталось {N} конфет')
        else:
            answerBot = fankBot(N)
            N = N - answerBot
            if N == 0:
                print('Поздравляем бот выиграл')
                break
            else:
                print(f'Бот взял себе {answerBot} конфет,осталось {N} конфет')
            answer1 = fankPlayer()
            N = N - answer1 
            if N == 0:
                print('Поздравляем, игрок выиграл')
                break
    else:
        print('досвидания игрок')
        break

