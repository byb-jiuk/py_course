Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Wallet:
    def __init__(self, amount=0):
        self.set_amount(amount)
    def get_amount(self):
        return self.amount
    def set_amount(self, value):
        if value < 0:
            pass
        self._amount = value

        
class NegaAmount(Exception):
    """Баланс отрицательный"""
    pass

raise NegaAmount
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    raise NegaAmount
NegaAmount
class Wallet:
    def __init__(self, amount=0):
        self.set_amount(amount)
    def get_amount(self):
        return self.amount
    def set_amount(self, value):
        if value < 0:
            raise NegaAmount
        self._amount = value

        
user1 = Wallet()
user1.__dict__
{'_amount': 0}
user2 = Wallet(100)
user2.__dict__
{'_amount': 100}
user2.get_amount()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    user2.get_amount()
  File "<pyshell#16>", line 5, in get_amount
    return self.amount
AttributeError: 'Wallet' object has no attribute 'amount'. Did you mean: '_amount'?
class Wallet:
    def __init__(self, amount=0):
        self.set_amount(amount)
    def get_amount(self):
        return self._amount
    def set_amount(self, value):
        if value < 0:
            raise NegaAmount
        self._amount = value

        
user1 = Wallet()
user2 = Wallet(100)
user1.get_amount()
0
user2.get_amount()
100
user2.set_amount(1000)
user2.set_amount(-1)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    user2.set_amount(-1)
  File "<pyshell#23>", line 8, in set_amount
    raise NegaAmount
NegaAmount
class Wallet:
    def __init__(self, amount=0):
        self.set_amount(amount)
    def get_amount(self):
        return self._amount
    def set_amount(self, value):
        if value < 0:
            raise NegaAmount
        self._amount = value
    amount = property(get_amount, set_amount)

    
user1 = Wallet()
user2 = Wallet(100)
user2.amount
100
user2.amount = 100000
user2.amount
100000
user2.__dict__
{'_amount': 100000}
class Wallet:
    def __init__(self, amount=0):
        self._amount = amount
    def get_amount(self):
        return self._amount
    def set_amount(self, value):
        if value < 0:
            raise NegaAmount
        self._amount = value
    amount = property(get_amount, set_amount)

    



def summ(a, b):
    return a + b

summ(4, 5)
9
def MyPrint(a,b,c):
    print(a,b,c)

    
MyPrint(1,2,3)
1 2 3
MyPrint(1,2,3,4)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    MyPrint(1,2,3,4)
TypeError: MyPrint() takes 3 positional arguments but 4 were given
help(print)
Help on built-in function print in module builtins:

print(*args, sep=' ', end='\n', file=None, flush=False)
    Prints the values to a stream, or to sys.stdout by default.

    sep
      string inserted between values, default a space.
    end
      string appended after the last value, default a newline.
    file
      a file-like object (stream); defaults to the current sys.stdout.
    flush
      whether to forcibly flush the stream.

def MyPrint(args):
    for val in args:
        print(val, end=" ")

        
def MyPrint(args):
    print(type(args))
    for val in args:
        print(val, end=" ")

        
MyPrint(1,2,3,4)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    MyPrint(1,2,3,4)
TypeError: MyPrint() takes 1 positional argument but 4 were given
MyPrint([1,2,3,4])
<class 'list'>
1 2 3 4 
MyPrint((1,2,3,4))
<class 'tuple'>
1 2 3 4 
def MyPrint(*args):
    print(type(args))
    for val in args:
        print(val, end=" ")

        
MyPrint([1,2,3,4])
<class 'tuple'>
[1, 2, 3, 4] 
MyPrint([1,2,3,4],1,3,2, True)
<class 'tuple'>
[1, 2, 3, 4] 1 3 2 True 
def MyPrint(*args):
    print(type(args))
    print(args)
    for val in args:
        print(val, end=" ")

        
MyPrint([1,2,3,4])
<class 'tuple'>
([1, 2, 3, 4],)
[1, 2, 3, 4] 
MyPrint(1,2,3,4)
<class 'tuple'>
(1, 2, 3, 4)
1 2 3 4 
MyPrint([1,2,3,4], 1,2,3, 3.14, True)
<class 'tuple'>
([1, 2, 3, 4], 1, 2, 3, 3.14, True)
[1, 2, 3, 4] 1 2 3 3.14 True 


help(print)
Help on built-in function print in module builtins:

print(*args, sep=' ', end='\n', file=None, flush=False)
    Prints the values to a stream, or to sys.stdout by default.

    sep
      string inserted between values, default a space.
    end
      string appended after the last value, default a newline.
    file
      a file-like object (stream); defaults to the current sys.stdout.
    flush
      whether to forcibly flush the stream.

def myPrint(*args, mySep=' ', myEnd='\n'):
    for val in args:
        print(val, end=mySep)
    print(end=myEnd)

    
myPrint()

print()

myPrint(1,2,3)
1 2 3 
print(1,2,3)
1 2 3
myPrint(1,2,3, [1,2,3,4], False)
1 2 3 [1, 2, 3, 4] False 
print(1,2,3, [1,2,3,4], False)
1 2 3 [1, 2, 3, 4] False
def summ(*args):
    res = 0
    for i in args:
        res += i
    return res

summ(1,2,3,45)
51
summ(1)
1
def cost_counter(*money):
    res = 0
    for i in money:
        res += i
    return res

def cost_counter(*money):
    res = 0
    for i in money:
        res += i
    return f"total cost: -{res}"

def cost_counter(*money):
    res = 0
    days = len(money)
    for i in money:
        res += i
    return f"total cost for {days} days is: -{res}\n"

cost_counter(15, 44, 100, 7, 3)
'total cost for 5 days is: -169\n'
cost_counter(15, 44, 100, 7, 3, 545, 58)
'total cost for 7 days is: -772\n'



# *args **kwargs

li = [1,2,3,4,5]
a, *b = li
b
[2, 3, 4, 5]


def family(**kwargs):
    print(kwargs)
    print(type(kwargs))

    
family(Nikola="dad", Maria="mom")
{'Nikola': 'dad', 'Maria': 'mom'}
<class 'dict'>
family(Nikola="dad", Maria="mom", 1=11)
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
family(Nikola="dad", Maria="mom", Sister=11)
{'Nikola': 'dad', 'Maria': 'mom', 'Sister': 11}
<class 'dict'>


# func (a,b,c, *args, **kwargs)
# func (**kwargs)
# func (*args, **kwargs)


def func(a,b,*args):
    print(a, type(a))
    print(b, type(b))
    print(args, type(args))

    
func(1,2,3,4,5,6,7,8)
1 <class 'int'>
2 <class 'int'>
(3, 4, 5, 6, 7, 8) <class 'tuple'>
def func(*args, a,b):
    print(a, type(a))
    print(b, type(b))
    print(args, type(args))

    
func(1,2,3,4,5,6,7,8)
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    func(1,2,3,4,5,6,7,8)
TypeError: func() missing 2 required keyword-only arguments: 'a' and 'b'
def func(*args, a=100,b=50):
    print(a, type(a))
    print(b, type(b))
    print(args, type(args))

    
func(1,2,3,4,5,6,7,8)
100 <class 'int'>
50 <class 'int'>
(1, 2, 3, 4, 5, 6, 7, 8) <class 'tuple'>
def func(a=100,b=50, *args):
    print(a, type(a))
    print(b, type(b))
    print(args, type(args))

    
func(1,2,3,4,5,6,7,8)
1 <class 'int'>
2 <class 'int'>
(3, 4, 5, 6, 7, 8) <class 'tuple'>
def func(a=100,b=50, *args, **kwargs):
    print(a, type(a))
    print(b, type(b))
    print(args, type(args))
    print(kwargs, type(kwargs))

    
func(1,2,3,4,5,6,7,8)
1 <class 'int'>
2 <class 'int'>
(3, 4, 5, 6, 7, 8) <class 'tuple'>
{} <class 'dict'>
func(1,2)
1 <class 'int'>
2 <class 'int'>
() <class 'tuple'>
{} <class 'dict'>
print()

func(1,2,3,4,5,6,7,8, dad="superhero", mom="batman")
1 <class 'int'>
2 <class 'int'>
(3, 4, 5, 6, 7, 8) <class 'tuple'>
{'dad': 'superhero', 'mom': 'batman'} <class 'dict'>








li1 = [1,2,3,4]
li2 = [3,4,5,6,7]
li3 = [li1, li2]
li3
[[1, 2, 3, 4], [3, 4, 5, 6, 7]]
li3 = [*li1, *li2]
li3
[1, 2, 3, 4, 3, 4, 5, 6, 7]
di1 = {1:11, 2:22}
di2 = {4:11, 5:22}
di3 = {**di1, **di2}
di3
{1: 11, 2: 22, 4: 11, 5: 22}
di3
{1: 11, 2: 22, 4: 11, 5: 22}
a, **b = di3
SyntaxError: invalid syntax
**b = di3
SyntaxError: invalid syntax





def converter(bitok):
    return bitok/3.5

converter
<function converter at 0x000002ACDA61AF20>
b1= 95000
converter(b1)
27142.85714285714
def converter(bitok):
    return bitok*3.5

converter(b1)
332500.0


lambda bitok: bitok*3.5
<function <lambda> at 0x000002ACDA61AF20>
(lambda bitok: bitok*3.5)(b1)
332500.0


1 + 999 +23423 * 4 + (lambda bitok: bitok*3.5)(b1)
427192.0




li = [1,2,3,4,5,6,7]
iterator = iter(li)
next
<built-in function next>
next(iterator)
1
next(iterator)
2
next(iterator)
3
next(iterator)
4
next(iterator)
5
next(iterator)
6
next(iterator)
7
next(iterator)
Traceback (most recent call last):
  File "<pyshell#199>", line 1, in <module>
    next(iterator)
StopIteration
for i in li:
    print(i)

    
1
2
3
4
5
6
7
help(list)
Help on class list in module builtins:

class list(object)
 |  list(iterable=(), /)
 |
 |  Built-in mutable sequence.
 |
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |
 |  Methods defined here:
 |
 |  __add__(self, value, /)
 |      Return self+value.
 |
 |  __contains__(self, key, /)
 |      Return bool(key in self).
 |
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |
 |  __eq__(self, value, /)
 |      Return self==value.
 |
 |  __ge__(self, value, /)
 |      Return self>=value.
 |
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |
 |  __getitem__(self, index, /)
 |      Return self[index].
 |
 |  __gt__(self, value, /)
 |      Return self>value.
 |
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  __iter__(self, /)
 |      Implement iter(self).
 |
 |  __le__(self, value, /)
 |      Return self<=value.
 |
 |  __len__(self, /)
 |      Return len(self).
 |
 |  __lt__(self, value, /)
 |      Return self<value.
 |
 |  __mul__(self, value, /)
 |      Return self*value.
 |
 |  __ne__(self, value, /)
 |      Return self!=value.
 |
 |  __repr__(self, /)
 |      Return repr(self).
 |
 |  __reversed__(self, /)
 |      Return a reverse iterator over the list.
 |
 |  __rmul__(self, value, /)
 |      Return value*self.
 |
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |
 |  __sizeof__(self, /)
 |      Return the size of the list in memory, in bytes.
 |
 |  append(self, object, /)
 |      Append object to the end of the list.
 |
 |  clear(self, /)
 |      Remove all items from list.
 |
 |  copy(self, /)
 |      Return a shallow copy of the list.
 |
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |
 |  extend(self, iterable, /)
 |      Extend list by appending elements from the iterable.
 |
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |
 |      Raises ValueError if the value is not present.
 |
 |  insert(self, index, object, /)
 |      Insert object before index.
 |
 |  pop(self, index=-1, /)
 |      Remove and return item at index (default last).
 |
 |      Raises IndexError if list is empty or index is out of range.
 |
 |  remove(self, value, /)
 |      Remove first occurrence of value.
 |
 |      Raises ValueError if the value is not present.
 |
 |  reverse(self, /)
 |      Reverse *IN PLACE*.
 |
 |  sort(self, /, *, key=None, reverse=False)
 |      Sort the list in ascending order and return None.
 |
 |      The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
 |      order of two equal elements is maintained).
 |
 |      If a key function is given, apply it once to each list item and sort them,
 |      ascending or descending, according to their function values.
 |
 |      The reverse flag can be set to sort in descending order.
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
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  __hash__ = None

# factorial !8
# 1 2 3 4 5 6 7 8


# febo


class Febo:
    def __init__(self, fn):
        self.fn = fn
        self.i = 0
        self.f1 = self.f2 = 1
    def __iter__(self):
        return self
    def __next__(self):
        self.i += 1
        if self.i > self.fn:
            raise StopIteration
        if self.i == 1 jr self.i == 2:
            
SyntaxError: invalid syntax
class Febo:
    def __init__(self, fn):
        self.fn = fn
        self.i = 0
        self.f1 = self.f2 = 1
    def __iter__(self):
        return self
    def __next__(self):
        self.i += 1
        if self.i > self.fn:
            raise StopIteration
        if self.i == 1 or self.i == 2:
            return 1
        fret = self.f1 + self.f2
        self.f1, self.f2 = self.f2. fret
        return fret

    
febx = Febo(10)
for f in febx:
    print(f, end=" ")

    
1 1 Traceback (most recent call last):
  File "<pyshell#232>", line 1, in <module>
    for f in febx:
  File "<pyshell#228>", line 15, in __next__
    self.f1, self.f2 = self.f2. fret
AttributeError: 'int' object has no attribute 'fret'
class Febo:
    def __init__(self, fn):
        self.fn = fn
        self.i = 0
        self.f1 = self.f2 = 1
    def __iter__(self):
        return self
    def __next__(self):
        self.i += 1
        if self.i > self.fn:
            raise StopIteration
        if self.i == 1 or self.i == 2:
            return 1
        fret = self.f1 + self.f2
        self.f1, self.f2 = self.f2, fret
        return fret

    
febx = Febo(10)
for f in febx:
    print(f, end=" ")

    
1 1 2 3 5 8 13 21 34 55 



li = [i ** 2 for i in range(10000)]
li

li = [i ** 2 for i in range(100)]
li
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401, 2500, 2601, 2704, 2809, 2916, 3025, 3136, 3249, 3364, 3481, 3600, 3721, 3844, 3969, 4096, 4225, 4356, 4489, 4624, 4761, 4900, 5041, 5184, 5329, 5476, 5625, 5776, 5929, 6084, 6241, 6400, 6561, 6724, 6889, 7056, 7225, 7396, 7569, 7744, 7921, 8100, 8281, 8464, 8649, 8836, 9025, 9216, 9409, 9604, 9801]
gen = (i ** 2 for i in range(100))
gen
<generator object <genexpr> at 0x000002ACDA62C1E0>
next(gen)
0
next(gen)
1
next(gen)

next(gen)
4
next(gen)

next(gen)
9
next(gen)

next(gen)
16
next(gen)

next(gen)
25
next(gen)
36
next(gen)
49
next(gen)
64
next(gen)
81
res = next(gen)
res
100
# gen expr


# func gen
def func(n):
    start = 0
    for i in range(n):
        start += 1
        return start

    
func(10)
1
def func(n):
    start = 0
    for i in range(n):
        start += 1
        return start

    
# return - return
# помнила прошлое - yield

func_gen = func(10)
func_gen
1
next(func_gen)
Traceback (most recent call last):
  File "<pyshell#281>", line 1, in <module>
    next(func_gen)
TypeError: 'int' object is not an iterator
def func(n):
    start = 0
    for i in range(n):
        start += 1
        yield start

        
func_gen = func(10)
func_gen
<generator object func at 0x000002ACDA5B3ED0>
next(func_gen)
1
next(func_gen)
2
next(func_gen)
3
next(func_gen)
4
next(func_gen)
5
def func(n):
    start = 0
    for i in range(n):
        start += 1
        yield start

        
for i in func(10):
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
gen = (i ** 2 for i in range(100))
gen = (i ** 2 for i in range(10))

for i in gen:
    print(i)

    
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



# map
# filter
# zip
help(zip)
Help on class zip in module builtins:

class zip(object)
 |  zip(*iterables, strict=False)
 |
 |  The zip object yields n-length tuples, where n is the number of iterables
 |  passed as positional arguments to zip().  The i-th element in every tuple
 |  comes from the i-th iterable argument to zip().  This continues until the
 |  shortest argument is exhausted.
 |
 |  If strict is true and one of the arguments is exhausted before the others,
 |  raise a ValueError.
 |
 |     >>> list(zip('abcdefg', range(3), range(4)))
 |     [('a', 0, 0), ('b', 1, 1), ('c', 2, 2)]
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
 |  __setstate__(self, object, /)
 |      Set state information for unpickling.
 |
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |
 |  __new__(*args, **kwargs)
 |      Create and return a new object.  See help(type) for accurate signature.



li = [1,2,3]
li2 = ["one", "two", "three"]
res_list = list(zip(li2, li))
res_list
[('one', 1), ('two', 2), ('three', 3)]
li = [1,2,3,4,5,6]
res_list = list(zip(li2, li))
res_list
[('one', 1), ('two', 2), ('three', 3)]



help(map)
Help on class map in module builtins:

class map(object)
 |  map(function, iterable, /, *iterables)
 |
 |  Make an iterator that computes the function using arguments from
 |  each of the iterables.  Stops when the shortest iterable is exhausted.
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
 |  Static methods defined here:
 |
 |  __new__(*args, **kwargs)
 |      Create and return a new object.  See help(type) for accurate signature.

li = [1,2,3,4,5,6,7,8]
li
[1, 2, 3, 4, 5, 6, 7, 8]
m = map(lambda x: x**2/2, li)
m
<map object at 0x000002ACDA61EB90>
li = list(m)
li
[0.5, 2.0, 4.5, 8.0, 12.5, 18.0, 24.5, 32.0]
for i in m:
    print(i)

    
m = map(lambda x: x**2/2, li)
for i in m:
    print(i)

    
0.125
2.0
10.125
32.0
78.125
162.0
300.125
512.0
gen = (i**2 for i in range(10))
for i in gen:
    print(i)

    
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
for i in gen:
    print(i)

    


help(filter)
Help on class filter in module builtins:

class filter(object)
 |  filter(function, iterable, /)
 |
 |  Return an iterator yielding those items of iterable for which function(item)
 |  is true. If function is None, return the items that are true.
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
 |  Static methods defined here:
 |
 |  __new__(*args, **kwargs)
 |      Create and return a new object.  See help(type) for accurate signature.




li = [1,2,3,4,5,6,7,8,9,10]
for i in filter(lambda x: x % 2 != 0, li):
    print(i)

    
1
3
5
7
9
for i in filter(lambda x: x % 2 == 0, li):
    print(i)

    
2
4
6
8
10




def func():
    number = 10
    return number

func()
10
def func():
    number = 10
    def inner():
        value = 5 + number
        return value
    return inner

func()
<function func.<locals>.inner at 0x000002ACDA6272E0>
result_inner_func = func()
result_inner_func
<function func.<locals>.inner at 0x000002ACDA627240>
result_inner_func()
15
result_inner_func
<function func.<locals>.inner at 0x000002ACDA627240>
result_inner_func.__closure__
(<cell at 0x000002ACDA61F7C0: int object at 0x00007FFDA60204C8>,)
def func1():
    number = 10
    return number

func1.__closure__
type
<class 'type'>
list
<class 'list'>
int
<class 'int'>
float
<class 'float'>
issubclass(float, object)
True
issubclass(list, object)
True
isinstance(float, object)
True
isinstance(float, type)
True
class D:
    pass


issubclass(D, object)
True
issubclass(D, list)
False
issubclass(D, float)
False
isinstance(D, float)
False
isinstance(D, int)
False
isinstance(D, type)
True
help(type)
Help on class type in module builtins:

class type(object)
 |  type(object) -> the object's type
 |  type(name, bases, dict, **kwds) -> a new type
 |
 |  Methods defined here:
 |
 |  __call__(self, /, *args, **kwargs)
 |      Call self as a function.
 |
 |  __delattr__(self, name, /)
 |      Implement delattr(self, name).
 |
 |  __dir__(self, /)
 |      Specialized __dir__ implementation for types.
 |
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  __instancecheck__(self, instance, /)
 |      Check if an object is an instance.
 |
 |  __or__(self, value, /)
 |      Return self|value.
 |
 |  __repr__(self, /)
 |      Return repr(self).
 |
 |  __ror__(self, value, /)
 |      Return value|self.
 |
 |  __setattr__(self, name, value, /)
 |      Implement setattr(self, name, value).
 |
 |  __sizeof__(self, /)
 |      Return memory consumption of the type object.
 |
 |  __subclasscheck__(self, subclass, /)
 |      Check if a class is a subclass.
 |
 |  __subclasses__(self, /)
 |      Return a list of immediate subclasses.
 |
 |  mro(self, /)
 |      Return a type's method resolution order.
 |
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |
 |  __prepare__(name, bases, /, **kwds)
 |      Create the namespace for the class statement
 |
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |
 |  __new__(*args, **kwargs)
 |      Create and return a new object.  See help(type) for accurate signature.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __abstractmethods__
 |
 |  __annotations__
 |
 |  __dict__
 |
 |  __text_signature__
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  __base__ = <class 'object'>
 |      The base class of the class hierarchy.
 |
 |      When called, it accepts no arguments and returns a new featureless
 |      instance that has no instance attributes and cannot be given any.
 |
 |
 |  __bases__ = (<class 'object'>,)
 |
 |  __basicsize__ = 928
 |
 |  __dictoffset__ = 264
 |
 |  __flags__ = 2155896066
 |
 |  __itemsize__ = 40
 |
 |  __mro__ = (<class 'type'>, <class 'object'>)
 |
 |  __type_params__ = ()
 |
 |  __weakrefoffset__ = 368

>>> 
>>> 
>>> 
>>> dog = type("Dog", (object,), {"counter":1})
>>> dog
<class '__main__.Dog'>
>>> dog.__name__
'Dog'
>>> dog.__dict__
mappingproxy({'counter': 1, '__module__': '__main__', '__dict__': <attribute '__dict__' of 'Dog' objects>, '__weakref__': <attribute '__weakref__' of 'Dog' objects>, '__doc__': None})
>>> dog.counter
1
>>> class Dog1:
...     counter=1
... 
...     
>>> d1 = dog()
>>> d1
<__main__.Dog object at 0x000002ACDA51ACF0>
>>> d2 = Dog1()
>>> d2
<__main__.Dog1 object at 0x000002ACDA51AE40>
