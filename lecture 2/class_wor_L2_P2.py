Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

#Task 3


1 == 1
True
1!=2
True
1 != 1
False
a = 55
a == 55
True
a != 66
True
b = 88
a == b
False
a != b
True


6 == 6
True
6!= 7
True
 res = 6 == 6
 
SyntaxError: unexpected indent
res = 6 == 6
res
True
type(res)
<class 'bool'>



2<3
True
2 <= 3
True
2 <= 2
True
2 < 2
False



2 * 4**2 < 55
True
2 * 4**2
32


5
5
5.0
5.0
5 == 5.
True
5 == 5.0000000000000000001
True



5 ==
SyntaxError: invalid syntax




password = input ("pass->")
pass->12345

password == "12345"
True

password == "123456"
False



#password



password = input ("pass->")
pass->123
if password == "123"
SyntaxError: expected ':'
if password == "123":
    print("Welcome!!")

    
Welcome!!
print(12)
12
password = input ("pass->")
pass->1
if password == "123":
    print("Welcome!!")

    
print (3123)
3123


password = input ("pass->")
pass->123
if password == "123":
    print("Welcome!!")
    print("Welcome!!")
    print("Welcome!!")

    
Welcome!!
Welcome!!
Welcome!!
password = input ("pass->")
pass->123
if password == "123":
    print("Welcome!!")
    print("Welcome!!")
    print("Welcome!!")
    
SyntaxError: multiple statements found while compiling a single statement
if password == "123":
    print("Welcome!!")
    print("Welcome!!")
    print("Welcome!!")
else:
    print("fail!!")

    
Welcome!!
Welcome!!
Welcome!!
password = input ("pass->")
pass->1
if password == "123":
    print("Welcome!!")
    print("Welcome!!")
    print("Welcome!!")
else:
    print("fail!!")

    
fail!!


password = input ("pass->")
pass->123
if password == "123":
    print("Welcome admin!!")
elif password == "321":
    print("Welcome manager!!")
else:
    print("fail!!")

    
Welcome admin!!
password = input ("pass->")
pass->123
if password == "321":
    print("Welcome admin!!")
elif password == "321":
    print("Welcome manager!!")
else:
    print("fail!!")

SyntaxError: multiple statements found while compiling a single statement
password = input ("pass->")
pass->321
if password == "123":
    print("Welcome admin!!")
elif password == "321":
    print("Welcome manager!!")
else:
    print("fail!!")

SyntaxError: multiple statements found while compiling a single statement
password = input ("pass->")
pass->321
if password == "123":
    print("Welcome admin!!")
elif password == "321":
    print("Welcome manager!!")
else:
    print("fail!!")

    
Welcome manager!!
password = input ("pass->")
pass->321
if password == "123":
    print("Welcome admin!!")
elif password == "321":
    print("Welcome manager!!")
elif password == "43":
    print("Welcome sup!!")    
else:
    print("fail!!")
    
SyntaxError: multiple statements found while compiling a single statement
password = input ("pass->")
pass->43
if password == "123":
    print("Welcome admin!!")
elif password == "321":
    print("Welcome manager!!")
elif password == "43":
    print("Welcome sup!!")    
else:
    print("fail!!")

    
Welcome sup!!



123 if 1 == 1 else 55
123
print (123 if 1 == 1 else 55)
123
password = input ("pass->")
pass->123
print (123 if password == "123": else 55)
SyntaxError: invalid syntax
password = input ("pass->")
123
SyntaxError: multiple statements found while compiling a single statement
password = input ("pass->")
pass->123
SyntaxError: multiple statements found while compiling a single statement
password = input ("pass->")
pass->123
print (123 if password == "123" else 55)
123
password = input ("pass->")
pass->321
print (123 if password == "123" else 55)
55



#task3


password = input ("pass->")
pass->123
password
'123'
match password:
    case "123":
        print("Welcome admin!!")
    case "321"
    
SyntaxError: expected ':'
match password:
    case "123":
        print("Welcome admin!!")
    case "321":
        print("Welcome me!!")
    case _:
        print("fail")

        
Welcome admin!!
password = input ("pass->")
pass->_
match password:
    case "123":
        print("Welcome admin!!")
    case "321":
        print("Welcome me!!")
    case _:
        print("fail")

        
fail
Welcome admin!!
SyntaxError: invalid syntax




help(while)
SyntaxError: invalid syntax



password = input ("pass->")
pass->123
>>> while password !=1:
...     print("bad pass. try again.")
...     password = input ("pass->")
... 
...     
bad pass. try again.
pass->3
bad pass. try again.
pass->555
bad pass. try again.
pass->7777
bad pass. try again.
pass->1
bad pass. try again.
pass->1
bad pass. try again.
pass->1
bad pass. try again.
pass->1
bad pass. try again.
pass->
bad pass. try again.
pass->1
bad pass. try again.
pass->1
bad pass. try again.
pass->
bad pass. try again.
pass->
bad pass. try again.
pass->
bad pass. try again.
pass->
bad pass. try again.
pass->
bad pass. try again.
pass->
bad pass. try again.
password = input ("pass->")
pass->123
while password !=1:
    print("bad pass. try.")
    password = input ("pass->")

    
bad pass. try.
pass->1
bad pass. try.
pass->6
bad pass. try.
pass->5
bad pass. try.
pass->4
bad pass. try.
pass->7
bad pass. try.
pass->3
bad pass. try.
pass->2
bad pass. try.
pass->1
bad pass. try.
pass->1
bad pass. try.
pass->
Traceback (most recent call last):
  File "<pyshell#4>", line 3, in <module>
    password = input ("pass->")
KeyboardInterrupt
password = int(input ("pass->"))
pass->123
while password !=1:
    print("bad pass. try.")
    password = input ("pass->")
    
SyntaxError: multiple statements found while compiling a single statement
password = int(input ("pass->"))
pass->123
while password !=1:
    print("bad pass. try.")
    password = input ("pass->")

    
bad pass. try.
pass->1
bad pass. try.
pass->2
bad pass. try.
pass->3
bad pass. try.
pass->
Traceback (most recent call last):
  File "<pyshell#8>", line 3, in <module>
    password = input ("pass->")
KeyboardInterrupt
counter = 10
while counter !=0:
    print(counter, end= " ")
    counter -=1

    
10 9 8 7 6 5 4 3 2 1 



a = 10
a = a - 1
a
9
a -= 1
a
8
a += 1
a
9
a *= 2
a
18


counter = 1
while counter < 10:
    print(counter ** 2)
    counter += 1

    
1
4
9
16
25
36
49
64
81
SyntaxError: multiple statements found while compiling a single statement

password = input ("pass->")
pass->123
while password !=1:
    print("bad pass. try.")
    password = input ("pass->")

    
bad pass. try.
pass->1
bad pass. try.
pass->6
bad pass. try.
pass->5
bad pass. try.
pass->4
bad pass. try.
pass->7
bad pass. try.
pass->3
bad pass. try.
pass->2
bad pass. try.
pass->1
bad pass. try.
pass->1
bad pass. try.
pass->
Traceback (most recent call last):
  File "<pyshell#4>", line 3, in <module>
    password = input ("pass->")
KeyboardInterrupt
password = int(input ("pass->"))
pass->123
while password !=1:
    print("bad pass. try.")
    password = input ("pass->")
    
SyntaxError: multiple statements found while compiling a single statement
password = int(input ("pass->"))
pass->123
while password !=1:
    print("bad pass. try.")
    password = input ("pass->")

    
bad pass. try.
pass->1
bad pass. try.
pass->2
bad pass. try.
pass->3
bad pass. try.
pass->
Traceback (most recent call last):
  File "<pyshell#8>", line 3, in <module>
    password = input ("pass->")
KeyboardInterrupt
counter = 10
while counter !=0:
    print(counter, end= " ")
    counter -=1

    
10 9 8 7 6 5 4 3 2 1 



a = 10
a = a - 1
a
9
a -= 1
a
8
a += 1
a
9
a *= 2
a
18


counter = 1
while counter < 10:
    print(counter ** 2)
    counter += 1

    
1
4
9
16
25
36
49
64
81
SyntaxError: multiple statements found while compiling a single statement

for 

for i in range (10):
    print(i**2)
    
SyntaxError: invalid syntax
for i in range (10):
    print(i**2)

    
0
1
4
9
16
25
36
49
64
81

for i in range (5, 10):
    print(i)

    
5
6
7
8
9


for i in range (5, 15):
    print(i)

    
5
6
7
8
9
10
11
12
13
14
for i in range (1, 15):
    print(i)

    
1
2
3
4
5
6
7
8
9
10
11
12
13
14
for i in range (1, 5, 15):
    print(i)

    
1
for i in range (1, 15, 2):
    print(i)

    
1
3
5
7
9
11
13



for i in range (1, 15, 2):
    if i % 2 == 0:
    print(i)
    
SyntaxError: expected an indented block after 'if' statement on line 2
for i in range (1, 15, 2):
    if i % 2 == 0:
        print(i)

        

for i in range (1, 15, 2):
    if i % 2 == 0:
        print(i)

        
for i in range (1, 15):
    if i % 2 == 0:
        print(i)

        
2
4
6
8
10
12
14
for i in range (1, 15):
    if i % 2 == 0:
        print(i)
        if i == 12:
            break

        
2
4
6
8
10
12
for i in range (1, 15):
    break
    if i % 2 == 0:
        print(i)
        if i == 12:
            break

        
break
SyntaxError: 'break' outside loop



for i in range (1, 15):
    if i % 2 == 0:
        continue
    print(i)

    
1
3
5
7
9
11
13


for i in range (1, 15):
    if i % 2 == 0:
        pass
    print(i)

    
1
2
3
4
5
6
7
8
9
10
11
12
13
14


for i in range (1, 15):
    if i % 2 == 0:
        break
    print(i)

    
1
for i in range (1, 15):
    if i % 2 == 0:
        continue
    print(i)

    
1
3
5
7
9
11
13


name = "Vasia"
"a" in name
True
"sia" in name
True
'v' in name
False
'v' in not name
SyntaxError: invalid syntax
'v' not in name
True


if "a" in name:
    print(123)

    
123


    
