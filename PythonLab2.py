#Работа со строками
string1 = "This is a string."
string2 = " This is another string."
string3 = string1 + string2
print(string3.upper())

##Извлечеение символов и подстрок
d = "qwerty"
ch = d[2] # извлекается символ ‘e’
chm = d[1:3], d[1:], d[:3], d[:], d[1:5:2]
#d[2] = 'o'
print(ch, chm)

#Работа с числами
x = 5
y = 25
z1 = x + y
z2 = x - y
z3 = x * y
z4 = x / y
z5 = x % y
z6 = 5 ** 5
print(z1, z2, z3, z4, z5, z6)
#param = "string" + 15
#print(param) #Python не выполняет автоматическое преобразование других типов.
#Нужно str(15)

#Преобразование данных
param = "string" + str(15)
#n1 = input("Enter the first number: ")
#n2 = input("Enter the second number: ")
#n3 = float(n1) + float(n2)
#print("Your result: " "{:100.3f}".format(n3))

##Форматирование строк
a = 1/3
print("{:7.3f}".format(a))
a = 2/3
b = 2/9
print("{:7.3f} {:7.3f}".format(a, b))
print("{:10.3e} {:10.3e}".format(a, b))

#Списки
list1 = [82,8,23,97,92,44,17,39,11,12]
#print(dir(list))
#print(help(list1))
list1.sort()
list1.append(444)
list1.insert(5, 545)
list1.remove(12)
list1.pop(-1)
print(list1)
##Сортировка элементов списка
list1.sort()
print(list1)
list2 = [3,5,6,2,33,6,11]
lis = sorted(list2)
print(lis)

#Кортежи
seq = (2,8,23,97,92,44,17,39,11,12)
seq.count(8)
seq.index(44)
print(seq)
listseq = list(seq)
print(type(listseq))

#Словари
D = {'food': 'Apple', 'quantity': 4, 'color': 'Red'}
D['food']
D['quantity'] += 10
print(D)
print(D['food'])

#dp1 = str(input("Enter the auto: "))
#dp2 = input("Enter the engine type: ")
#dp3 = input("Enter the age: ")
#dp = {'name': dp1, 'engineType': dp2, 'age': int(dp3)}
#print(dp['name'])
#dp['age'] += 29
#print(dp)



#Вложенность хранения данных
rec = {'name': {'firstname': 'Bob', 'lastname': 'Smith'},
            'job': ['dev', 'mgr'],
            'age': 25}
print(rec['name'])
print(rec['name']['firstname'])
print(rec['job'])
rec['job'].append('janitor')
print(rec['name']['firstname'], rec['name']['lastname'], rec['job'], rec['age'])

