Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
for i in range(10):
    print(i)
else:
    print('Цикл завершился успешно.')

    
0
1
2
3
4
5
6
7
8
9
Цикл завершился успешно.
for i in range(10):
    if number == 7:
        break
    print(i)
    
else:
    print('Цикл завершился успешно.')

    
Traceback (most recent call last):
  File "<pyshell#6>", line 2, in <module>
    if number == 7:
NameError: name 'number' is not defined
for i in range(10):
    if number == 7:
        break
    print(i)
else:
    print('Цикл завершился успешно.')

    
Traceback (most recent call last):
  File "<pyshell#8>", line 2, in <module>
    if number == 7:
NameError: name 'number' is not defined
for i in range(10):
    if i == 7:
        break
    print(i)
else:
    print('Цикл завершился успешно.')

    
0
1
2
3
4
5
6

counter = 10
while counter > 0:
    print (counter)
    counter -=1

    
10
9
8
7
6
5
4
3
2
1
counter = 10
while counter > 0:
    print (counter)
    counter -=1
    
SyntaxError: multiple statements found while compiling a single statement
while counter > 0:
    print (counter)
    counter -=1
else:
    print('Цикл завершился успешно.')

    
Цикл завершился успешно.



Цикл завершился успешно.
SyntaxError: invalid syntax
while counter > 0:
        if counter == 5:
        break
    print(counter)
    counter -= 1
else:
    print('Цикл завершился успешно.')
    
SyntaxError: expected an indented block after 'if' statement on line 2
counter = 10
while counter > 0:
        if counter == 5:
        break
    print(counter)
    counter -= 1
else:
    print('Цикл завершился успешно.')
    
SyntaxError: expected an indented block after 'if' statement on line 2
while counter > 0:
        if counter == 5:
            break
        print(counter)
        counter -= 1
else:
    print('Цикл завершился успешно.')

    
10
9
8
7
6



a = 10
a > 10
False
a > 5
True
c = 5
a
10
c
5
a == 10
True
c == 5
True
a == 10 and c == 5
True
c > 5
False
a == 10 and c > 5
False
a > 10 and c > 5
False


True and True
True
False and True
False
False and False
False
box = 100
waller = 200
if wallet > 0 and wallet >= box:
    print("pay")
else:
    print ("fault")

    
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    if wallet > 0 and wallet >= box:
NameError: name 'wallet' is not defined. Did you mean: 'waller'?
box = 100
wallet= 200
if wallet > 0 and wallet >= box:
    print("pay")
else:
    print ("fault")
    
SyntaxError: multiple statements found while compiling a single statement
if wallet > 0 and wallet >= box:
    print("pay")
else:
    print ("fault")

    
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    if wallet > 0 and wallet >= box:
NameError: name 'wallet' is not defined. Did you mean: 'waller'?
wallet = 200
bos = 100
if wallet > 0 and wallet >= box:
    print("pay")
else:
    print ("fault")

    
pay
time = "day"
if wallet > 0 and wallet >= box and time == "day":
    print("pay")
else:
    print ("fault")

    
pay
time = "night"
if wallet > 0 and wallet >= box and time == "day":
    print("pay")
else:
    print ("fault")

    
fault
if wallet > 0 and wallet >= box:
    if time == "day":
        print("pay")
    else:
        print("fail by time")
else:
    print ("fault balance")

    
fail by time




counter1 = 10
counter2 = 15
while counter1 > 0 or counter2 > 0:
    if counter1> 0:
        print ("pervyi", counter1)
    else:
        print("pervyi otval")
    if counter2 > 0:
        print ("vtoroy", counter2)
    else:    
        print ("vtoroy otval")

        
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
pervyi 10
vtoroy 15
Traceback (most recent call last):
  File "<pyshell#83>", line 7, in <module>
    print ("vtoroy", counter2)
KeyboardInterrupt
while counter1 > 0 or counter2 > 0:
    if counter1> 0:
        print ("pervyi", counter1)
    else:
        print("pervyi otval")
    if counter2 > 0:
        print ("vtoroy", counter2)
    else:    
        print ("vtoroy otval")
    counter1 -=1
    counter2 -=1

    
pervyi 10
vtoroy 15
pervyi 9
vtoroy 14
pervyi 8
vtoroy 13
pervyi 7
vtoroy 12
pervyi 6
vtoroy 11
pervyi 5
vtoroy 10
pervyi 4
vtoroy 9
pervyi 3
vtoroy 8
pervyi 2
vtoroy 7
pervyi 1
vtoroy 6
pervyi otval
vtoroy 5
pervyi otval
vtoroy 4
pervyi otval
vtoroy 3
pervyi otval
vtoroy 2
pervyi otval
vtoroy 1
while counter1 > 0 or counter2 > 0:
    if counter1> 0:
        print ("pervyi", counter1)
    else:
        print("pervyi otval")
    if counter2 > 0:
        print ("vtoroy", counter2)
    else:    
        print ("vtoroy otval")
    counter1 -=1
    counter2 -=1

    
counter1= 3
counter2 = 6
while counter1 > 0 and counter2 > 0:
    if counter1> 0:
        print ("pervyi", counter1)
    else:
        print("pervyi otval")
    if counter2 > 0:
        print ("vtoroy", counter2)
    else:    
        print ("vtoroy otval")
    counter1 -=1
    counter2 -=1

    
pervyi 3
vtoroy 6
pervyi 2
vtoroy 5
pervyi 1
vtoroy 4
5 > 2
True
3< 5
True
True or False
True
True and False
False
True and True
True





True
True
not True
False
not False
True
3 > 2
True
not 3 > 2
False
if 3> 2:
    print(3)
else:
    print(2)

    
3
if not 3> 2:
    print(3)
else:
    print(2)

    
2
not not not not True
True
not 3 > 2 or not 5< 6
False
not not not 3 > 2 or not not 5< 6
True





#calc
# exit + - * / while input int float print

number1 = int(input("Введи число:"))
Введи число:12
number2 = int(input("Введи число:"))
Введи число:6
operation = input("+ - * / exit")
+ - * / exit+
operation
'+'
if operation == "+":
    print (number1 + number2)

    
18
if operation == "+":
    print (number1 + number2)
elif operation == "-":
    print (number1 - number2)
elif operation == "*":
    print (number1 * number2)
elif operation == "/":
    print (number1 / number2)
else:
    print ("Dont under...")

    
18
operation = input("+ - * / exit")
+ - * / exit+
while operation != "exit":
    number1 = int(input("Введи число:"))
    number2 = int(input("Введи число:"))
    if operation == "+":
        print (number1 + number2)
    elif operation == "-":
        print (number1 - number2)
    elif operation == "*":
        print (number1 * number2)
    elif operation == "/":
        print (number1 / number2)
    else:
        print ("Dont under...")

        
Введи число:5
Введи число:4
9
Введи число:4
Введи число:2
6
Введи число:exit
Traceback (most recent call last):
  File "<pyshell#146>", line 2, in <module>
    number1 = int(input("Введи число:"))
ValueError: invalid literal for int() with base 10: 'exit'
while operation != "exit":
    number1 = int(input("Введи число:"))
    number2 = int(input("Введи число:"))
    if operation == "+":
        print (number1 + number2)
    elif operation == "-":
        print (number1 - number2)
    elif operation == "*":
        print (number1 * number2)
    elif operation == "/":
        print (number1 / number2)
    else:
        print ("Dont under...")
    operation = input("+ - * / exit")

    
Введи число:5
Введи число:4
9
+ - * / exit*
Введи число:4
Введи число:2
8
+ - * / exitexit




while operation != "exit":
    number1 = int(input("Введи число:"))
    number2 = int(input("Введи число:"))
    if operation == "+":
        print (number1 + number2)
    elif operation == "-":
        print (number1 - number2)
    elif operation == "*":
        print (number1 * number2)
    elif operation == "/":
        print (number1 / number2)
    else:
        print ("Dont under...")
    operation = input("+ - * / exit")

    

operation = input("+ - * / exit")
+ - * / exit+
while operation != "exit":
    number1 = int(input("Введи число:"))
    number2 = int(input("Введи число:"))
    if operation == "+":
        print (number1 + number2)
    elif operation == "-":
        print (number1 - number2)
    elif operation == "*":
        print (number1 * number2)
    elif operation == "/":
        print (number1 / number2)
    else:
        print ("Dont under...")
    operation = input("+ - * / exit")

    
Введи число:5
Введи число:6
11
+ - * / exit/
Введи число:18
Введи число:3
6.0
+ - * / exit*
Введи число:5
Введи число:5
25
+ - * / exiteixt
Введи число:5
Введи число:6
Dont under...
+ - * / exit*
Введи число:5
Введи число:6
30
+ - * / exitexit
while operation != "exit":
    number1 = int(input("Введи число:"))
    number2 = int(input("Введи число:"))
    if operation == "+":
        print (number1 + number2)
    elif operation == "-":
        print (number1 - number2)
    elif operation == "*":
        print (number1 * number2)
    elif operation == "/":
        print (number1 / number2)
    else:
        print ("Dont under...")
    operation = input("+ - * / exit")

    
operation = input("+ - * / exit")
+ - * / exit
while operation != "exit":
    number1 = int(input("Введи число:"))
    number2 = int(input("Введи число:"))
    if operation == "+":
        print (number1 + number2)
    elif operation == "-":
        print (number1 - number2)
    elif operation == "*":
        print (number1 * number2)
    elif operation == "/":
        print (number1 / number2)
    else:
        print ("Dont under...")
    operation = input("+ - * / exit")

    
Введи число:5
Введи число:6
Dont under...
+ - * / exit8
Введи число:5
Введи число:6
Dont under...
+ - * / exit+
Введи число:5
Введи число:6
11
+ - * / exitexit
operation = input("+ - * / exit")
+ - * / exit
while operation != "exit":
    number1 = int(input("Введи число:"))
    number2 = int(input("Введи число:"))
    if operation == "+":
        print (number1 + number2)
    elif operation == "-":
        print (number1 - number2)
    elif operation == "*":
        print (number1 * number2)
    elif operation == "/":
        print (number1 / number2)
    else:
        print ("Dont understand...")
    operation = input("+ - * / exit")

    
Введи число:5
Введи число:6
Dont understand...
+ - * / exit*
Введи число:6
Введи число:5
30
+ - * / exitexit







#lists

a = 1
f = 2.14
s = "adasd"
li = [3, 6 , "asasd", True, f, s, a]
li
[3, 6, 'asasd', True, 2.14, 'adasd', 1]
type(li)
<class 'list'>
# list_name [index]
li[0]
3
li[3]
True
li[6]
1
li[4]
2.14
li[10]
Traceback (most recent call last):
  File "<pyshell#188>", line 1, in <module>
    li[10]
IndexError: list index out of range


li = []
li
[]
li = list()
li
[]
li = [3,4,5,7,9]
li[0]
3
li [-1]
9
li [-3]
5


s = "abc"
s
'abc'
print (1)
1
print (s)
abc
s.upper()
'ABC'
a = 10
a.upper()
Traceback (most recent call last):
  File "<pyshell#207>", line 1, in <module>
    a.upper()
AttributeError: 'int' object has no attribute 'upper'



li1 = [1,2,3,4]
li2 = [True, False, "asd"]
li1+li2
[1, 2, 3, 4, True, False, 'asd']
res = li1+li2
res
[1, 2, 3, 4, True, False, 'asd']
li1 * 9
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
li1 *= 4
li1
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
li2 += li2*3
li2
[True, False, 'asd', True, False, 'asd', True, False, 'asd', True, False, 'asd']
len
<built-in function len>
help(len)
Help on built-in function len in module builtins:

len(obj, /)
    Return the number of items in a container.

li1
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
len(li1)
16
li1[15]
4
li1[len(li1)]
Traceback (most recent call last):
  File "<pyshell#226>", line 1, in <module>
    li1[len(li1)]
IndexError: list index out of range
li1 [len(li1)-1]
4
li = [1,2,3,4]
li[1]
2
li[1] = 22
li
[1, 22, 3, 4]
li.append(555)
li
[1, 22, 3, 4, 555]
li.insert(3, 333)
li
[1, 22, 3, 333, 4, 555]
li.insert(2, 444)
li
[1, 22, 444, 3, 333, 4, 555]
li.sort()
li
[1, 3, 4, 22, 333, 444, 555]
li.reverse()
li
[555, 444, 333, 22, 4, 3, 1]
li.pop ()
1
li.pop()
3
res = li.pop()
res
4
li
[555, 444, 333, 22]
li.pop (0)
555
li
[444, 333, 22]
li = [1,2,]
li = [1,2,3,4,5]
li
[1, 2, 3, 4, 5]
li.remove(2)
li
[1, 3, 4, 5]
li.pop(222222)
Traceback (most recent call last):
  File "<pyshell#254>", line 1, in <module>
    li.pop(222222)
IndexError: pop index out of range
val = 2222
if val in li:
    li.remove(2222)
else:
    print("2222 nety")

    
2222 nety
li
[1, 3, 4, 5]
li.index(3)
1
li.index(213213)
Traceback (most recent call last):
  File "<pyshell#263>", line 1, in <module>
    li.index(213213)
ValueError: 213213 is not in list
li = [1,1,1,1]
li.index(1)
0
li.remove(1)
li
[1, 1, 1]
li.clear()
li
[]
li = [1,1,1,1]
del li[1]
li
[1, 1, 1]
del li
li
Traceback (most recent call last):
  File "<pyshell#274>", line 1, in <module>
    li
NameError: name 'li' is not defined


hat_list = [1,2,3,4,5]
hat_list.len
Traceback (most recent call last):
  File "<pyshell#278>", line 1, in <module>
    hat_list.len
AttributeError: 'list' object has no attribute 'len'
len(hat_list)
5
hat_list.insert(2, 111)
hat_list
[1, 2, 111, 3, 4, 5]
hat_list.remove(5)
hat_list
[1, 2, 111, 3, 4]
len(hat_list)
5
print(hat_list)
[1, 2, 111, 3, 4]


li = [1,2,3,4,5,6,7,8,9]
li
[1, 2, 3, 4, 5, 6, 7, 8, 9]
# by value

for value in li:
    print(value, end=" |")

    
1 |2 |3 |4 |5 |6 |7 |8 |9 |
for value in li:
    print(5+value**2, end=" |")

    
6 |9 |14 |21 |30 |41 |54 |69 |86 |
st = "sdsadsadad"
st[0]
's'
's'
's'
st[1]
'd'
for i in st:
    print(i, end=" |")

    
s |d |s |a |d |s |a |d |a |d |
#by

li
[1, 2, 3, 4, 5, 6, 7, 8, 9]
len(5)
Traceback (most recent call last):
  File "<pyshell#306>", line 1, in <module>
    len(5)
TypeError: object of type 'int' has no len()
len(li)
9
for i in range(len(li)):
    print(li[i])

    
1
2
3
4
5
6
7
8
9
total = 0
for i in range(len(li)):
    total + = li[i]
    
SyntaxError: invalid syntax

for i in range(len(li)):
    total += li[i]

    
total = 0
for i in range(len(li)):
    total += li[i]

    
total
45
for i in li:
    total += i

    
total
90

# 4 5 2 3 1
# 1 2 3 4 5

a = 8
b = 3

a = b
b = a
a
3
b
3
a = 8
b = 3
tmp = a
tmp
8
a = b
a
3
b = tmp
b
8



a = 8
b = 3
a, b = b,a
a
3
b
8
# 4 5 2 3 1

li = [4,5,2,3,1]
li[1], li [2] = li[2], li[1]
li
[4, 2, 5, 3, 1]
li[2], li [3] = li[3], li[2]
li
[4, 2, 3, 5, 1]
li[3], li [4] = li[4], li[3]
li
[4, 2, 3, 1, 5]
li[0], li [1] = li[1], li[0]
il
Traceback (most recent call last):
  File "<pyshell#360>", line 1, in <module>
    il
NameError: name 'il' is not defined
li
[2, 4, 3, 1, 5]
li[1], li [2] = li[2], li[1]
li
[2, 3, 4, 1, 5]
li[2], li [3] = li[3], li[2]
li
[2, 3, 1, 4, 5]









li = [1, 2,3,4,5]
li2 = li.copy()
li
[1, 2, 3, 4, 5]
li2
[1, 2, 3, 4, 5]
li[0] = 111
li
[111, 2, 3, 4, 5]
li2
[1, 2, 3, 4, 5]
li = [1, 2,3,4,5]
li2 = [3,4,5, li]
li
[1, 2, 3, 4, 5]
li2
[3, 4, 5, [1, 2, 3, 4, 5]]
li3 = li2.copy()
li3
[3, 4, 5, [1, 2, 3, 4, 5]]
li[0] = 9999
li
[9999, 2, 3, 4, 5]
li3
[3, 4, 5, [9999, 2, 3, 4, 5]]
from copy import deep copy
SyntaxError: invalid syntax
from copy import deepcopy
li = [1, 2,3,4,5]
li2 = [3,4,5, li]
li3 = deepcopy(li2)
li3
[3, 4, 5, [1, 2, 3, 4, 5]]
li
[1, 2, 3, 4, 5]
li[0] = 9999
li3
[3, 4, 5, [1, 2, 3, 4, 5]]



li = [1,2,3,4,5,6,7,8,9,7,8,5,4,8,6,]
li
[1, 2, 3, 4, 5, 6, 7, 8, 9, 7, 8, 5, 4, 8, 6]
li[:]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 7, 8, 5, 4, 8, 6]
li[2:]
[3, 4, 5, 6, 7, 8, 9, 7, 8, 5, 4, 8, 6]
li[3:6]
[4, 5, 6]
res = li[3:6]
res
[4, 5, 6]




li= [1,2,3,4,5,6,7,8,9,7,8,5,4,8,6,]
li2 = [True, False,True, False,True, False]
li3 = ["sdfsfs","sdfsfs","sdfsfs","sdfsfs",]

res = li[:3] + li2[2:5] + li3[2:]
res
[1, 2, 3, True, False, True, 'sdfsfs', 'sdfsfs']



li
[1, 2, 3, 4, 5, 6, 7, 8, 9, 7, 8, 5, 4, 8, 6]
#in not in
li_to_find = 5
li_to_find in li
True



li
[1, 2, 3, 4, 5, 6, 7, 8, 9, 7, 8, 5, 4, 8, 6]
li[-6:-2]
[7, 8, 5, 4]
li
[1, 2, 3, 4, 5, 6, 7, 8, 9, 7, 8, 5, 4, 8, 6]
del li[-6:-2]
li
[1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 6]



>>> se = set()
>>> se
set()
>>> print(se)
set()
>>> se = {1,2,3,4,5,1,2,3,4,5}
>>> se
{1, 2, 3, 4, 5}
>>> len(se)
5
>>> 6 in se
False
>>> 5 in se
True
>>> 1 in se
True
>>> for i in se:
...     print (i)
... 
...     
1
2
3
4
5
>>> se.add(444)
>>> se.add(4445)
>>> se
{1, 2, 3, 4, 5, 444, 4445}
>>> se.update ({5,6,7,8,3,4,})
>>> se
{1, 2, 3, 4, 5, 6, 7, 8, 444, 4445}
>>> se.remove(4)
>>> se
{1, 2, 3, 5, 6, 7, 8, 444, 4445}
>>> se.remove(44)
Traceback (most recent call last):
  File "<pyshell#457>", line 1, in <module>
    se.remove(44)
KeyError: 44
>>> se.discard(3)
>>> se
{1, 2, 5, 6, 7, 8, 444, 4445}
>>> se.discard(33)
>>> 
>>> se
{1, 2, 5, 6, 7, 8, 444, 4445}
