from random import randint
import time

#Ввод имен играющих
def enter_name():
    return input()

#Бросаем кубик
def thr_game(user, n):
    print('Кубик бросает', user)
    time.sleep(1)
    n = randint(1, 6)
    print('Выпало: ', n)
    return n

#Выводим результатт
def result_game(res1,res2,smbd1, smbd2):
    if res1 > res2:
        print('Выиграл', smbd1)
    elif res1 < res2:
        print('Выиграл', smbd2)
    else:
        print('Ничья')