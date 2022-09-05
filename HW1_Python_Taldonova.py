# 1. Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# n = int(input('Введите цифру от 1 до 7: '))
# if (n > 1 and n <= 5):
#     print('День недели не выходной')
# elif (n > 5 and n <= 7):
#     print('День недели выходной')

# 2. Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

#for x in range(0,1):
#    for y in range(0,1):
#        for z in range(0,1):
#            print (not(x or y or z) == ((not x) and (not y) and (not z)))

# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# x = int(input('Введите координаты X: '))
# y = int(input('Введите координаты Y: '))

# if (x != 0 and y != 0):
#     if x > 0 and y > 0:
#         print('Четверть - 1')
#     if x < 0 and y > 0:
#         print('Четверть - 2')
#     if x < 0 and y < 0:
#         print('Четверть - 3')  
#     if x > 0 and y < 0:
#          print('Четверть - 4')
# else:
#     print('Точка лежит на оси координат')

# 4. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

# n = int(input('Введите номер четверти от 1 до 4: '))
# if n == 1:
#     print("x > 0 и y > 0")
# if n == 2:
#     print('x < 0 и y > 0')
# if n == 3:  
#     print('x < 0 and y < 0')
# if n == 4:   
#     print('x > 0 and y < 0')

# 5. Напишите программу, которая принимает на вход координаты двух точек и 
# находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# Теорема Пифагора
# ab^2 = ac^2 + bc^2
# AB = кв корень из (ac^2 + bc^2)

xa = int(input('Введите координаты x(a): '))
ya = int(input('Введите координаты y(a): '))
xb = int(input('Введите координаты x(b): '))
yb = int(input('Введите координаты y(b): '))

ac = ya - yb
bc = xa - xb

print(int((ac ** 2 + bc ** 2) ** 0.5*100)/100)