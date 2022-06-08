#Работа с оператором ветвления
from random import randint
import time

#Ввод имен играющих
igrok1 = input('Введите имя 1-го играющего ')
igrok2 = input('Введите имя 2-го играющего ')



#Моделирование бросание кубика первым играющим
t1 = 0
for n1 in range(5):
    print('Кубик бросает', igrok1)
    time.sleep(1)
    n1 = randint(1, 6)
    print('Выпало: ', n1)
    if n1 >= 1 and n1 <= 6:
        t1 += n1 #t1 = t1 + n1
print(t1)

#Моделирование бросания кубика вторым играющим
t2 = 0
for z in range(5):
    print('Кубик бросает', igrok2)
    time.sleep(2)
    n2 = randint(1, 6)
    print('Выпало:', n2)
    if n2 >= 1 and n2 <= 6:
        t2 += n2  # t2 = t2 + n2
print(t2)
if t1 > t2:
     print('Выиграл', igrok1)
elif t1 < t2:
     print('Выиграл', igrok2)
else:
     print('Ничья')


#if n1 > n2:
  #  print('Выиграл', igrok1)
#elif n1 < n2:
  #  print('Выиграл', igrok2)
#else:
   # print('Ничья')




