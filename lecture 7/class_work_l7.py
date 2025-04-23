Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.


1+ 1
2
4234 * 5
21170
li = [1,2,3,4,5]
li
[1, 2, 3, 4, 5]
print(li)
[1, 2, 3, 4, 5]
li[0]
1
li[-1]
5
name = 1231354
if name == 1231354:
    print(name)
else:
    print(False)

    
1231354



def name_checker(name):
    if name == "secret":
        return True
    else:
        return False

    
name = "sdasd"
name_checker(name)
False
def name_checker(name):
    if name == "secret":
        return True
    return False

name_checker(name)
False
def name_checker(name):
    return name == "secret"

name_checker(name)
False
name_checker("secret")
True




enumerate
<class 'enumerate'>
help(enumerate)
Help on class enumerate in module builtins:

class enumerate(object)
 |  enumerate(iterable, start=0)
 |
 |  Return an enumerate object.
 |
 |    iterable
 |      an object supporting iteration
 |
 |  The enumerate object yields pairs containing a count (from start, which
 |  defaults to zero) and a value yielded by the iterable argument.
 |
 |  enumerate is useful for obtaining an indexed list:
 |      (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
 |
 |  Methods defined here:
 |
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |
 |  __iter__(self, /)
 |      Implement iter(self).
 |
 |  __next__(self, /)
 |      Implement next(self).
 |
 |  __reduce__(self, /)
 |      Return state information for pickling.
 |
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |
 |  __class_getitem__(object, /)
 |      See PEP 585
 |
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |
 |  __new__(*args, **kwargs)
 |      Create and return a new object.  See help(type) for accurate signature.



li
[1, 2, 3, 4, 5]
for value in li:
    print(value)

    
1
2
3
4
5
for value in range(len(li)):
    print(i)

    
Traceback (most recent call last):
  File "<pyshell#45>", line 2, in <module>
    print(i)
NameError: name 'i' is not defined
for i in range(len(li)):
    print(i)

    
0
1
2
3
4
for i, v in enumerate(li):
    print(i, v)

    
0 1
1 2
2 3
3 4
4 5
for i, v in enumerate(li):
    print(i, v)
    print(li[i])

    
0 1
1
1 2
2
2 3
3
3 4
4
4 5
5
for i, v in enumerate(li, 5):
    print(i, v)

    
5 1
6 2
7 3
8 4
9 5



bool
<class 'bool'>
bool(1)
True
bool(2)
True
bool(0)
False
bool(-4)
True
bool()
False
bool(" ")
True
bool("")
False
bool([])
False
indicator_list = [1, 2, 3, 4, 5, 6]
indicator_list = [1, 0, 1, 1, 0, 1]
bool(indicator_list[0])
True
bool(indicator_list[1])
False
if bool(indicator_list[0]) and bool(indicator_list[1]) and bool(indicator_list[2]) and bool(indicator_list[3]) and bool(indicator_list[4]) and bool(indicator_list[5]):
    print("OK")
else:
    print("Bad")

    
Bad
indicator_list = [1, 1, 1, 1, 1, 1]
if bool(indicator_list[0]) and bool(indicator_list[1]) and bool(indicator_list[2]) and bool(indicator_list[3]) and bool(indicator_list[4]) and bool(indicator_list[5]):
    print("OK")
else:
    print("Bad")

    
OK
# all any
# all - каждый елемент и прогоняет через bool
# если везде True

if all(indicator_list ):
    print("OK")
else:
    print("Bad")

    
OK
indicator_list = [1, 0, 1, 1, 0, 1]
if all(indicator_list ):
    print("OK")
... else:
...     print("Bad")
... 
...     
Bad
>>> 
>>> 
>>> # any
... # any - каждый елемент и прогоняет через bool
... # если хотя бы один 1 = True  - возвращает rue
>>> indicator_list = [1, 0, 1, 1, 0, 1]
>>> any(indicator_list)
True
>>> indicator_list = [0, 0, 0, 0, 0, 1]
>>> any(indicator_list)
True
>>> indicator_list = [0, 0, 0, 0, 0, 0]
>>> any(indicator_list)
False
>>> 
>>> 
>>> 
>>> def my_all(iterable):
...     flag = None
...     for value in iterable:
...         if not bool(value):
...             return False
...         flag = True
...     return flag
... 
>>> li
[1, 2, 3, 4, 5]
>>> my_all(li)
True
>>> li = [1, 2, 3, 4, 5, 0]
>>> my_all(li)
False
>>> my_all([1,2,3,4,0,44])
False
