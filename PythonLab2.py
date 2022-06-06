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
n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
n3 = float(n1) + float(n2)
print("Your result: " "{:100.3f}".format(n3))

##Форматирование строк
a = 1/3
print("{:7.3f}".format(a))
a = 2/3
b = 2/9
print("{:7.3f} {:7.3f}".format(a, b))
print("{:10.3e} {:10.3e}".format(a, b))