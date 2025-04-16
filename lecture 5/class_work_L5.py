Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# functions

1+3
4
print (12)
12
type(3)
<class 'int'>
3 < 5
True
666 > 55
True
input()
sdasdad
'sdasdad'
int("12313")
12313
li = [1,2,3,4,5]
li
[1, 2, 3, 4, 5]
li[0]
1
li[-1]
5
li.append(23423)
li
[1, 2, 3, 4, 5, 23423]
li.pop()
23423
se = {1,2,3,4,5}
se.add(55)
se.add(4)
se
{1, 2, 3, 4, 5, 55}



#sing up


#name , phone, username
# 10 users
# per day
name = input("Name:")
Name:Vasia
name = input("Phone:")
Phone:123121354
name = input("Username:")
Username:asdasdasd
user1 = [name,phone,username]
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    user1 = [name,phone,username]
NameError: name 'phone' is not defined. Did you mean: 'None'?
user1 = [Name,Phone,Username]
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    user1 = [Name,Phone,Username]
NameError: name 'Name' is not defined. Did you mean: 'name'?



def sing_up():
    name = input("Name:")
    phone = input("Phone:")
    username = input("Username:")
    user = [name, phone. username]
    print("User:", user, "was created.")

    
sing_up
<function sing_up at 0x0000025E4FAA1D00>
def sing_up():
    name = input("Name:")
    phone = input("Phone:")
    username = input("Username:")
    user = [name, phone, username]
    print("User:", user, "was created.")

    
sing_up
<function sing_up at 0x0000025E4FAA1BC0>
sing_up()
Name:Sasha
Phone:123121
Username:byblik
User: ['Sasha', '123121', 'byblik'] was created.
sing_up()
Name:Sana
Phone:454546
Username:sanok
User: ['Sana', '454546', 'sanok'] was created.



def hel lo():
    
SyntaxError: expected '('
def hello:
    
SyntaxError: expected '('
def hello()
SyntaxError: expected ':'
def hello():
    print ("Hello")

    
def bye():
    print ("Goodbye!")

    
hello()
Hello
bye()
Goodbye!
for i in range(5):
    hello()
    bye()

    
Hello
Goodbye!
Hello
Goodbye!
Hello
Goodbye!
Hello
Goodbye!
Hello
Goodbye!



bye
<function bye at 0x0000025E4FAA1A80>
del bye
bye
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    bye
NameError: name 'bye' is not defined
def sing_up():
    name = input("Name:")
    phone = input("Phone:")
    username = input("Username:")
    user = [name, phone, username]
    print("User:", user, "was created.")

    

print("Hi user.")
Hi user.
1+3
4
5+5
10
if 1 == 1:
    sing_up()

    
Name:123
Phone:123
Username:123
User: ['123', '123', '123'] was created.
56564
56564
6+6+6
18

hello
<function hello at 0x0000025E4FAA19E0>
type(hello)
<class 'function'>
hello = 10
type(hello)
<class 'int'>
hello
10
hello()
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    hello()
TypeError: 'int' object is not callable


print = 100
print()
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    print()
TypeError: 'int' object is not callable

================================ RESTART: Shell ================================
print()

print()

print(1,2,3,4,5, end=" ")
1 2 3 4 5 
# cm --> m
#178 --> 1.78
def converter_cm_to_m():
    pass

def hello_user(user_name):
    print("welcome, {user_name}")

    
hello_user("Vasia")
welcome, {user_name}
def hello_user(user_name):
    print(f"welcome, {user_name}")

    
hello_user("Vasia")
welcome, Vasia
hello_user("Vasia", "Pupkin")
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    hello_user("Vasia", "Pupkin")
TypeError: hello_user() takes 1 positional argument but 2 were given
def converter_cm_to_m(cm):
    cmm = cm%100    mm = cm // 100
    
SyntaxError: invalid syntax
def converter_cm_to_m(cm):
    cmm = cm%100 #78
    mm = cm // 100 #1
    print(mm, cmm, sep=".")

    
converter_cm_to_m(178)
1.78
converter_cm_to_m(164)
1.64

cmm
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    cmm
NameError: name 'cmm' is not defined
mm
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    mm
NameError: name 'mm' is not defined
cm
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    cm
NameError: name 'cm' is not defined
if True:
    a= 1000

    
a
1000



def fun(num1, st1, li1):
    print(num1, st1, li1)
    bbbb = 10000
    print(bbbb)

    
num1
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    num1
NameError: name 'num1' is not defined
bbbb
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    bbbb
NameError: name 'bbbb' is not defined
fun(1, "sdasdsa", [1,2,34])
1 sdasdsa [1, 2, 34]
10000
fun(1, "sdasdsa")
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    fun(1, "sdasdsa")
TypeError: fun() missing 1 required positional argument: 'li1'
fun(1, [1,2,34])
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    fun(1, [1,2,34])
TypeError: fun() missing 1 required positional argument: 'li1'




# simple
def hello(name, phone):
    print("Name:", name)
    print("phone:", phone)

    
hello("Vasia", 123124)
Name: Vasia
phone: 123124
hello(123124, "Vasia")
Name: 123124
phone: Vasia



def sing_up(name, phone, username):
    user = [name, phone, username]
    print("User:", user, "was created.")

    
sing_up("dsff", 123123)
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    sing_up("dsff", 123123)
TypeError: sing_up() missing 1 required positional argument: 'username'
def sing_up(phone, username, name="Jonny"):
    user = [name, phone, username]
    print("User:", user, "was created.")

    
sing_up(1231564, "fdsfsdfs")
User: ['Jonny', 1231564, 'fdsfsdfs'] was created.
sing_up(123123,"dfsdfdsf","petr")
User: ['petr', 123123, 'dfsdfdsf'] was created.



def feedback(name, phone, comment="", email=""):
    print(name, phone)
    print(comment,email)

    
feedback("Sasha", 12312345)
Sasha 12312345
 
feedback("Sasha", 12312345, "sdfsdfsfsfsdfsf", "@")
Sasha 12312345
sdfsdfsfsfsdfsf @







# while exit +- funcs



def add(a, b):
    print(f"{a} + {b} = {a+b}")

    
des sub(a, b):
    
SyntaxError: invalid syntax
def sub(a, b):
    print(f"{a} - {b} = {a-b}")

    
def mul(a,b):
    print(f"{a} * {b} = {a*b}")

    
oper = input("exit + -")
exit + -
while oper != "exit":
    num1, num2 = int(input("n1:")), int(input("n2:"))
    if oper == "+":
        add(num1, num2)
    elif oper == "-":
        sub(num1, num2)
    elif oper == "*":
        mul(num1, num2)
    else:
        print("erorr!")
    oper = input("exit + -")

    
n1:5
n2:2
erorr!
exit + -+
n1:5
n2:2
5 + 2 = 7
exit + -
n1:1
n2:1
erorr!
exit + -exit




def add(a, b):
    print(f"{a} + {b} = {a+b}")

    
name = input("name:")
name:Vasia
name
'Vasia'
summa = add(a, 5)
1000 + 5 = 1005
summa
print(summa)
None
def add(a, b):
    print(f"{a} + {b} = {a+b}")
    return a+b

summa = add(4, 5)
4 + 5 = 9
summa
9
def hello(name):
    return "Welcome, " + name

greetings = hello("Vasia")
greetings
'Welcome, Vasia'
def add(a, b):
    print(f"{a} + {b} = {a+b}")
    return a+b

def sub(a, b):
    print(f"{a} - {b} = {a-b}")
    return a-b

def mul(a,b):
    print(f"{a} * {b} = {a*b}")
    return a * b

def main():
    while oper != "exit":
        num1, num2 = int(input("n1:")), int(input("n2:"))
        if oper == "+":
            result = add(num1, num2)
            print("result return:", result)
        elif oper == "-":
            result = sub(num1, num2)
            print("result return:", result)
        elif oper == "*":
            result = mul(num1, num2)
            print("result return:", result)
        else:
            print("erorr!")
        oper = input("exit + -")

        
main()
Traceback (most recent call last):
  File "<pyshell#241>", line 1, in <module>
    main()
  File "<pyshell#240>", line 2, in main
    while oper != "exit":
UnboundLocalError: cannot access local variable 'oper' where it is not associated with a value
def main():
    oper = input("exit + - *")
    while oper != "exit":
        num1, num2 = int(input("n1:")), int(input("n2:"))
        if oper == "+":
            result = add(num1, num2)
            print("result return:", result)
        elif oper == "-":
            result = sub(num1, num2)
            print("result return:", result)
        elif oper == "*":
            result = mul(num1, num2)
            print("result return:", result)
        else:
            print("erorr!")
        oper = input("exit + -")

        
main()
exit + - *+
n1:5
n2:4
5 + 4 = 9
result return: 9
exit + -5
n1:4
n2:5
erorr!
exit + -exit


pass
def shallow():
    pass

shallow()
res = shallow()
print(res)
None
def converter_cm_to_m(cm):
    cmm = cm%100 #78
    mm = cm // 100 #1
    print(mm, cmm, sep=".")

    
def converter_cm_to_m(cm):
    cmm = cm%100 #78
    mm = cm // 100 #1
    return f"{mm}.{cmm}"
res = converter_cm_to_m(122)
SyntaxError: invalid syntax
def converter_cm_to_m(cm):
    cmm = cm%100 #78
    mm = cm // 100 #1
    return f"{mm}.{cmm}"

res = converter_cm_to_m(122)
res
'1.22'
input
<built-in function input>
help(input)
Help on built-in function input in module builtins:

input(prompt='', /)
    Read a string from standard input.  The trailing newline is stripped.

    The prompt string, if given, is printed to standard output without a
    trailing newline before reading input.

    If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
    On *nix systems, readline is used if available.

def converter_cm_to_m(cm):
    """Эта функция для ковертции роста в см в строку с метрами.
    Arguments:
    cm - int rost v cm.
    Returns:
    str- stroka c metrami."""
    
    cmm = cm%100 #78
    mm = cm // 100 #1
    
    return f"{mm}.{cmm}"

help(converter_cm_to_m)
Help on function converter_cm_to_m in module __main__:

converter_cm_to_m(cm)
    Эта функция для ковертции роста в см в строку с метрами.
    Arguments:
    cm - int rost v cm.
    Returns:
    str- stroka c metrami.




def converter_cm_to_m(cm):
    """Эта функция для ковертции роста в см в строку с метрами.
    Arguments:
    cm - int rost v cm.
    Returns:
    str- stroka c metrami pri cm >= 100.
    False - bool pri cm< 100.
    """
    
    if cm < 100:
        return False
    cmm = cm%100 #78
    mm = cm // 100 #1
    
    return f"{mm}.{cmm}"

converter_cm_to_m(99)
False
converter_cm_to_m(100)
'1.0'
converter_cm_to_m(1000)
'10.0'
def converter_cm_to_m(cm):
    """Эта функция для ковертции роста в см в строку с метрами.
    Arguments:
    cm - int rost v cm.
    Returns:
    str- stroka c metrami pri cm >= 100.
    False - bool pri cm< 100.
    """
    return 1000
    if cm < 100:
        return False
    cmm = cm%100 #78
    mm = cm // 100 #1
    
    return f"{mm}.{cmm}"

converter_cm_to_m(10)
1000
converter_cm_to_m(-1000)
1000
def converter_cm_to_m(cm):
    """Эта функция для ковертции роста в см в строку с метрами.
    Arguments:
    cm - int rost v cm.
    Returns:
    str- stroka c metrami pri cm >= 100.
    False - bool pri cm< 100.
    """
    if cm < 100:
        return False
    cmm = cm%100 #78
    mm = cm // 100 #1
    
    return f"{mm}.{cmm}"




li = [1,2,3,4]
li2 = li
li2[0] = 999
li
[999, 2, 3, 4]
li2
[999, 2, 3, 4]




def fun(listik):
    listik[0] = 19999

    
li
[999, 2, 3, 4]
fun(li)
li
[19999, 2, 3, 4]
li = [1,2,3,4]
fun(li[:])
li
[1, 2, 3, 4]
fun(li.copy())
li
[1, 2, 3, 4]
from copy import deepcopy
fun(deepcopy(li))
li
[1, 2, 3, 4]



isinstance
<built-in function isinstance>
help(isinstance)
Help on built-in function isinstance in module builtins:

isinstance(obj, class_or_tuple, /)
    Return whether an object is an instance of a class or of a subclass thereof.

    A tuple, as in ``isinstance(x, (A, B, ...))``, may be given as the target to
    check against. This is equivalent to ``isinstance(x, A) or isinstance(x, B)
    or ...`` etc.


isinstance(10, int)
True
isinstance("sdsadad", list)
False
isinstance(li , list)
True
isinstance(5.6 , float)
True

total = 0
def add_to_total(n):
    total = total + n

    
add_to_total(5)
Traceback (most recent call last):
  File "<pyshell#322>", line 1, in <module>
    add_to_total(5)
  File "<pyshell#321>", line 2, in add_to_total
    total = total + n
UnboundLocalError: cannot access local variable 'total' where it is not associated with a value
def add_to_total(n):
    total = total + n

    
add_to_total(5)
Traceback (most recent call last):
  File "<pyshell#325>", line 1, in <module>
    add_to_total(5)
  File "<pyshell#324>", line 2, in add_to_total
    total = total + n
UnboundLocalError: cannot access local variable 'total' where it is not associated with a value
def add_to_total(n):
    total = total + n
add_to_total(5)
SyntaxError: invalid syntax
def add_to_total(n):
    total = total + n
add_to_total(5)
SyntaxError: invalid syntax
total
0
def add_to_total(n):
    result = total + n
    print(result)

    
add(5)
Traceback (most recent call last):
  File "<pyshell#333>", line 1, in <module>
    add(5)
TypeError: add() missing 1 required positional argument: 'b'
def add(n):
    result = total + n
    print(result)

    
add(5)
5
def add_to_total(n):
    result = total + n
    print(result)

    
total = 9
def add(n):
    global total
    total = total + n

    
add(5)
total
14



name = 100
def hello(name):
    print(name)

    
name
100
hello(name)
100
first_name = 1000
def hello(f_name):
    print(f_name)

    
hello(first_name)
1000
first_name
1000
f_name
Traceback (most recent call last):
  File "<pyshell#361>", line 1, in <module>
    f_name
NameError: name 'f_name' is not defined. Did you mean: 'name'?


# !5 !6 !3
1 * 3 * 2
6
1 * 3 * 2 * 4 * 5
120
# !10
1 * 3 * 2 * 4 * 5 *6 *7 *8 *9 *10
3628800
1 * 3 * 2 * 4 * 5 *6 *7 *8 *9
362880
!9
SyntaxError: invalid syntax


def factorial(n):
    if n < 0:
        return
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

factorial(9)
362880
factorial(0)
1
factorial(2)
2
factorial(-2)
def main():
    oper = input("exit +")
    while oper != "exit":
        factorial(int(input("factorial to number:")))
        print("factorial is:", result)
        oper = input("exit +")

        
main()
exit ++
factorial to number:10
Traceback (most recent call last):
  File "<pyshell#391>", line 1, in <module>
    main()
  File "<pyshell#390>", line 5, in main
    print("factorial is:", result)
NameError: name 'result' is not defined
def main():
    oper = input("exit +")
    while oper != "exit":
        result = factorial(int(input("factorial to number:")))
        print("factorial is:", result)
        oper = input("exit +")

        
main()
exit ++
factorial to number:10
factorial is: 3628800
exit +exit








def recurs (n):
    if n >= 20:
        return 1
    return n + recurs(n + 4)

#recurs (1)
#1 +  recurs(1 + 4) = recurs(5)
#1 + 5 + recurs(5+4) = recurs(9)
#1 + 5 + 9 +recurs(9+4) = recurs(13)
#1 + 5 + 9 + 13 + recurs(13+4)
#1 + 5 + 9 + + 13 +17 recurs(13+4)
#1 + 5 + 9 + + 13 +17 + 1
#46

recurs(1)
46
def factorial(n):
    if n < 0:
        return
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

# factorial(5)
# 5 * 4 * factorial(5 - 1)

factorial(5)
120
import sys
sys.getrecursionlimit()
1000



f1, f2 = 1, 1
f1, f2 = f2, f1 + f2
f2
2
f1, f2 = f2, f1 + f2
f2
3
f1, f2 = f2, f1 + f2
f2
5
f1, f2 = f2, f1 + f2
f2
8
n = 3
for i in range(2, n):
    pass

f1, f2 = 1, 1
for i in range(2, n):
...     f1, f2 = f2, f1 + f2
... 
...     
>>> f2
2
>>> n = 4
>>> f1, f2 = 1, 1
>>> for i in range(2, n):
...     f1, f2 = f2, f1 + f2
... 
...     
>>> f2
3
>>> n = 5
>>> f1, f2 = 1, 1
>>> for i in range(2, n):
...     f1, f2 = f2, f1 + f2
... 
...     
>>> f2
5
>>> 
>>> 
>>> def febo(n):
...     f1, f2 = 1, 1
...     if n < 0:
...         return
...     if n == 1 or n == 2:
...         return 1
...     for i in range(2, n):
...         f1, f2 = f2, f1 + f2
...     return f2
... 
>>> febo(5)
5
>>> febo(6)
8
>>> febo(7)
13
