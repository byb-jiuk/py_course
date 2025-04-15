Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

help (input)
Help on built-in function input in module builtins:

input(prompt='', /)
    Read a string from standard input.  The trailing newline is stripped.

    The prompt string, if given, is printed to standard output without a
    trailing newline before reading input.

    If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
    On *nix systems, readline is used if available.

result = input ("Введи пароль:")
Введи пароль:12345
print(result)
12345
type(result)
<class 'str'>

result = input()
12345

result
'12345'
result = input ("Введи пароль:")
Введи пароль:12345

number1 = input("Дай первое число:")
Дай первое число:55

type (number1)
<class 'str'>
number1 - 44
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    number1 - 44
TypeError: unsupported operand type(s) for -: 'str' and 'int'


a = 10

a = int(10)

a
10
a = int(10.5)
a
10
a = int ("10")
a
10
type (a)
<class 'int'>

a = int ("-10")
a
-10
a = int ("-10a")
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a = int ("-10a")
ValueError: invalid literal for int() with base 10: '-10a'
f  = 10.5
f
10.5
f = float(10)
f
10.0
f = float("10")
f
10.0
f = float("10.5555")
f
10.5555
f = float(10.555)
f
10.555
s = str(a)
s
'-10'
s=str(f)
s
'10.555'
print (s)
10.555
s
'10.555'


print (s)
10.555
print (type(s))
<class 'str'>
print (s, type(s))
10.555 <class 'str'>
print (a, type(a))
-10 <class 'int'>
print (repr(s), type(s))
'10.555' <class 'str'>
print (repr(a), type(a))
-10 <class 'int'>








#Task 1

result = input("Введи число:")
Введи число:123
print (repr(number), type(number))
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    print (repr(number), type(number))
NameError: name 'number' is not defined. Did you mean: 'number1'?
number = int (number)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    number = int (number)
NameError: name 'number' is not defined. Did you mean: 'number1'?
number = input("Введи число:")
Введи число:123
number - 99
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    number - 99
TypeError: unsupported operand type(s) for -: 'str' and 'int'
number = int (input(" Введи Число:"))
 Введи Число:321
number2 = int(input("Введи число:"))
Введи число:55
result = number + number2
print (result)
376


num = 0.
num
0.0
num=.555
num
0.555


2 ** 3
8
2 ** 3 ** 2
512

8**2
64
3 ** 2
9
2 ** 9
512


9 / 5
1.8
9 / 0
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    9 / 0
ZeroDivisionError: division by zero
0 / 9
0.0
9 // 0
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    9 // 0
ZeroDivisionError: integer division or modulo by zero
9 % 0
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    9 % 0
ZeroDivisionError: integer modulo by zero



s = "hello"
s2= "fds"
s+s2
'hellofds'

res = s+ s2

res
'hellofds'



s * 5
'hellohellohellohellohello'
5 * s
'hellohellohellohellohello'

res2 = s + s1 * 5
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    res2 = s + s1 * 5
NameError: name 's1' is not defined
res2 = s + s2 * 5
res2
'hellofdsfdsfdsfdsfds'

number = int (input(" Введи Число:"))
 Введи Число:555
number * 5
2775
number = int (input(" Введи Число:"))
 Введи Число:555
number * 5
2775
number = input(" Введи Число:")
 Введи Число:555
number * 5
'555555555555555'


s = "sdsds"\
"sdfsdfs"
s = ("sdsds"
"sdfsdfs")
s = "sdsds"
# "sdfsdfs"
s
'sdsds'
s = "sdsds"\
"sdfsdfs"\
"dadadad"\
"sdadsad"
s
'sdsdssdfsdfsdadadadsdadsad'
s = ("sdsds"
"sdfsdfs"
"dadadad"
"sdadsad")
s
'sdsdssdfsdfsdadadadsdadsad'



a = 5
b = 9
c = 99
print(a, "+", b, "+", c, "=", a+b+c)
5 + 9 + 99 = 113
f"{a} + {b} = {a+b}"
'5 + 9 = 14'
print(f"{a} + {b} + {c} = {a+b+c}")
5 + 9 + 99 = 113




#task2 programma


a = 99
b = 888

a, b = 99, 888
a
99
b
888
a, b = int(input ("->")), float(input("->"))
->55
->99.8
a
55
>>> b
99.8
>>> a = 1
>>> b = 1
>>> c = 1
>>> a = b = c = 1
>>> a
1
>>> b
1
>>> 
>>> 
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
