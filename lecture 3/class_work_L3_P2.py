# Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.



# #lecture 3 class work

# for f in sorted(set(basket)):
#     print(f)

    
# Traceback (most recent call last):
#   File "<pyshell#7>", line 1, in <module>
#     for f in sorted(set(basket)):
# NameError: name 'basket' is not defined
# basket = {apple,banana,orange,pear}
# Traceback (most recent call last):
#   File "<pyshell#8>", line 1, in <module>
#     basket = {apple,banana,orange,pear}
# NameError: name 'apple' is not defined. Did you mean: 'tuple'?
# basket = {'apple','banana','orange','pear'}
# basket
# {'apple', 'orange', 'pear', 'banana'}
# for f in sorted(set(basket)):
#     print(f)

    
# apple
# banana
# orange
# pear

# li = [55, 66, 5, 55, 6]
# li
# [55, 66, 5, 55, 6]
# li = set(li)
# li
# {66, 5, 6, 55}
# li = list(li)
# li
# [66, 5, 6, 55]
# #Сначала сделали список, из списка set , он удалил повторяющиеся, потом снова сделали список
# a = set ('asddfgdfgd')
# b
# Traceback (most recent call last):
#   File "<pyshell#22>", line 1, in <module>
#     b
# NameError: name 'b' is not defined
# a
# {'g', 'a', 'd', 'f', 's'}
# a.sort
# Traceback (most recent call last):
#   File "<pyshell#24>", line 1, in <module>
#     a.sort
# AttributeError: 'set' object has no attribute 'sort'
# a = list(a)
# a
# ['g', 'a', 'd', 'f', 's']
# a.sort
# <built-in method sort of list object at 0x00000177A45BBB00>
# a
# ['g', 'a', 'd', 'f', 's']
# sort(a)
# Traceback (most recent call last):
#   File "<pyshell#29>", line 1, in <module>
#     sort(a)
# NameError: name 'sort' is not defined
# li.sort()
# li
# [5, 6, 55, 66]
# a = set(a)
# a
# {'g', 'a', 'd', 'f', 's'}
# a.sort()
# Traceback (most recent call last):
#   File "<pyshell#34>", line 1, in <module>
#     a.sort()
# AttributeError: 'set' object has no attribute 'sort'
# a = list(a)
# a
# ['g', 'a', 'd', 'f', 's']
# a.sort()
# a
# ['a', 'd', 'f', 'g', 's']
# a = set(a)
# a
# {'g', 'a', 'd', 'f', 's'}
# a = 666
# myset = set(a)
# Traceback (most recent call last):
#   File "<pyshell#42>", line 1, in <module>
#     myset = set(a)
# TypeError: 'int' object is not iterable
# a = 'fhfhfh'
# myset = set(a)
# myset
# {'h', 'f'}
# a = 'f'
# myset = set(a)
# a
# 'f'
# a = 777
# mylist = list(a)
# Traceback (most recent call last):
#   File "<pyshell#50>", line 1, in <module>
#     mylist = list(a)
# TypeError: 'int' object is not iterable
# a = 'fhfhfh'
# mylist = list(a)
# mylist
# ['f', 'h', 'f', 'h', 'f', 'h']
# a = 'j'
# mylist = list(a)
# mylist
# ['j']
# ['j']
# ['j']
# a = True
# set(a)
# Traceback (most recent call last):
#   File "<pyshell#59>", line 1, in <module>
#     set(a)
# TypeError: 'bool' object is not iterable
# list(a)
# Traceback (most recent call last):
#   File "<pyshell#60>", line 1, in <module>
#     list(a)
# TypeError: 'bool' object is not iterable
# a = [1,2,1,2,3]
# a
# [1, 2, 1, 2, 3]
# set(a)
# {1, 2, 3}
# se = {1,2,3}
# list(se)
# [1, 2, 3]
# str(se)
# '{1, 2, 3}'
# str(a)
# '[1, 2, 1, 2, 3]'
# int(se)
# Traceback (most recent call last):
#   File "<pyshell#68>", line 1, in <module>
#     int(se)
# TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
# a
# [1, 2, 1, 2, 3]
# int(a)
# Traceback (most recent call last):
#   File "<pyshell#70>", line 1, in <module>
#     int(a)
# TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
# my_list = [1,2,4,4,1,4,2,6,2,9]
# res_list = []

# my_list = set(my_list)
# my_list
# {1, 2, 4, 6, 9}
# my_list = list(my_list)
# my_list
# [1, 2, 4, 6, 9]



# li = []
# for value in range (1, 11):
#     li.append(value)

    
# li
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# #в пустой список выше, включили значения от 1 до 11 не включая 11 с помощью for



# li = []
# for value in range(1, 11):
#     if value % 2 == 0:
#         li.append(value)

        
# li
# [2, 4, 6, 8, 10]
# #включение в пустой список значений на цело делящихся на 2[2, 4, 6, 8, 10]


# li = [value for value in range(1, 11)]
# li
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# li = [value for value in range(1, 11) if value % 2 == 0]
# li
# [2, 4, 6, 8, 10]
# # то же самое что и два примера выше только в одну строку


# squares = [x ** 2 for x in range(10)]
# print (squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# twos = [2 ** i for i in range(8)]
# print (twos)
# [1, 2, 4, 8, 16, 32, 64, 128]
# #граемся со стпенями


# scores = [input() for i in range(5)]
# 55
# 6
# 7
# 99
# 5
# scores
# ['55', '6', '7', '99', '5']
# scores = [int(input()) for i in range (5)]
# 66
# 77
# 88
# 9
# 4
# scores
# [66, 77, 88, 9, 4]
# # создали списки введением чисел как строка, а затем int - ом тоже самое только числа




# squares = [x ** 2 for x in range(10)]
# odds = [x for x in squares if x % 2 !=0]

# print(odds)
# [1, 9, 25, 49, 81]





# q = int(input())
# 5
# qq = [float(input(f'{i} -->')) for i in range(q)]
# 0 -->55
# 1 -->2.55
# 2 -->4.9
# 3 -->5
# 4 -->7
# qq
# [55.0, 2.55, 4.9, 5.0, 7.0]
# type(qq[0])
# <class 'float'>
# qq = [float(input(f'{i} -->')) for i in range(int(input()))]
# 3
# 0 -->4
# 1 -->5
# 2 -->6
# qq
# [4.0, 5.0, 6.0]
# qq = [int(input(f'{i} -->')) for i in range(int(input()))]
# 2
# 0 -->1
# 1 -->2
# qq
# [1, 2]
# qq = [str(input(f'{i} -->')) for i in range(int(input()))]
# 2
# 0 -->1
# 1 -->3
# qq
# ['1', '3']
# #создаем список с созданием ренжа, который сами задаем и прописываем значения



# number_string = '1 2 3 4 5'
# number_string.split()
# ['1', '2', '3', '4', '5']
# number_string
# '1 2 3 4 5'
# number_string = '1,2,3,4,5'
# number_string
# '1,2,3,4,5'
# separator = ','
# number_string.split(separator)
# ['1', '2', '3', '4', '5']
# number_string
# '1,2,3,4,5'


# numbers = [value for value in input().split()]
# 7 6 555 -9 888
# numbers
# ['7', '6', '555', '-9', '888']
# numbers = [int(value) for value in input().split()]
# 7 6 655 -9 88
# numbers
# [7, 6, 655, -9, 88]


# st = input()
# 3 4 5 58456486846 53
# st.split()
# ['3', '4', '5', '58456486846', '53']
# st
# '3 4 5 58456486846 53'




# #home work 3.5 split()
# li = input('put string of numbers by space:')
# put string of numbers by space: 4 -55 888 -212
# li = input('put string of numbers by space:').split()
# put string of numbers by space: 4 -55 888 -212
# Li = [int(val) for val in li]
# Li
# [4, -55, 888, -212]
# S = sum(Li)
# print(S)
# 625



# a = {x for x in 'abracadabra'}
# a
# {'c', 'a', 'd', 'r', 'b'}
# a = {x for x in 'abracadabra' if x not in 'abc'}
# a
# {'d', 'r'}


# li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# to_find = 5
# found = False


# for i in range(len(li)):
#     found = li[i] == to_find
#     if found:
#         break

    
# if found:
#     print("Elem found at index", i)
# else:
#     print("absent")

    
# Elem found at index 4



# drawn = [5, 11, 9, 42, 3, 49]
# bets = [3, 7, 11, 42, 34, 49]
# hits = 0

# for number in bets:
#     if number in drawn:
#         hits += 1

        
# print(hits)
# 4


# a = set ('qwerty')
# b = frozenset('qwerty')
# a == b
# True
# True
# True
# type(a - b)
# <class 'set'>
# type (a | b)
# <class 'set'>
# a.add(1)
# a
# {1, 'e', 'q', 'r', 'y', 'w', 't'}
# b.add(1)
# Traceback (most recent call last):
#   File "<pyshell#223>", line 1, in <module>
#     b.add(1)
# AttributeError: 'frozenset' object has no attribute 'add'


# li = [[1, 2], [3, 4], [5, 6]]
# li
# [[1, 2], [3, 4], [5, 6]]
# li[0]
# [1, 2]
# li [0][0]
# 1
# li[1]
# [3, 4]
# li[1][1]
# 4
# >>> 
# >>> 
# >>> 
# >>> 
# >>> table = [[":(", ":)", ":(", ":)"],]
# >>> table = [[":(", ":)", ":(", ":)"],
# ...          [":)", ":(", ":)", ":)"],
# ...          [":(", ":)", ":)", ":("],
# ...          [":)", ":)", ":)", ":("]]
# >>> print(table)
# [[':(', ':)', ':(', ':)'], [':)', ':(', ':)', ':)'], [':(', ':)', ':)', ':('], [':)', ':)', ':)', ':(']]
# >>> print(table[0][0])
# :(
# >>> print(table[1][1])
# :(
# >>> print(table[1][2])
# :)
# >>> 
# >>> cube = [[[':(', 'x', 'x'],
# ...          [':)', 'x', 'x'],
# ...          [':(', 'x', 'x']],
# ...         [[':)', 'x', 'x'],
# ...          [':(', 'x', 'x'],
# ...          [':)', 'x', 'x']],
# ...         [[':(', 'x', 'x'],
# ...          [':)', 'x', 'x'],
# ...          [':(', 'x', 'x']]]
# >>> print(cube)
# [[[':(', 'x', 'x'], [':)', 'x', 'x'], [':(', 'x', 'x']], [[':)', 'x', 'x'], [':(', 'x', 'x'], [':)', 'x', 'x']], [[':(', 'x', 'x'], [':)', 'x', 'x'], [':(', 'x', 'x']]]
# >>> print(cube[0][0][0])
# :(
# >>> print(cube[2][2][0])
# :(
# >>> 
# >>> 
# >>> 
# >>> a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# >>> print(a)
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# >>> print(a[1])
# [4, 5, 6]
# >>> print(a[2])
# [7, 8, 9]
# >>> print(a[0])
# [1, 2, 3]
# >>> print()

