from random import randint
import time

#Ввод имен играющих
def enterName():
    return input()

#Бросаем кубик
def thrGame(user, n):
    print('Кубик бросает', user)
    time.sleep(1)
    n = randint(1, 6)
    print('Выпало: ', n)
    return n

#Выводим результатт
def resultGame(res1,res2,smbd1, smbd2):
    if res1 > res2:
        print('Выиграл', smbd1)
    elif res1 < res2:
        print('Выиграл', smbd2)
    else:
        print('Ничья')

igrok1 = enterName()
igrok2 = enterName()
score1 = 0
score2 = 0
resultGame(thrGame(igrok1, score1), thrGame(igrok2, score2), igrok1, igrok2)


