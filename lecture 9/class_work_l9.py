Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
32 + 25
57
66 /55
1.2
"dfsdfsf"
'dfsdfsf'
li = ["sfsfdsf"]
li
['sfsfdsf']
# CRM
# Client - name phone email
client1 = ["Dima", 37537337337, "dimas@di,a.dima"]
clien1[0]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    clien1[0]
NameError: name 'clien1' is not defined. Did you mean: 'client1'?
client1[0]
'Dima'
client1[1]
37537337337
client1[2]
'dimas@di,a.dima'
client2 = ["dfgdfgfdg", 37537337337, "sdfsdf@di,a.dima"]
client3 = ["Dima", 3753733454547337, "dimas@di,a.dima"]
client4 = ["sdfsfsfsf", "Dima", "dimas@di,a.dima","address"]
client4[0]
'sdfsfsfsf'



a = 10
type(a)
<class 'int'>
b = 123
type(b)
<class 'int'>
a + b
133




# Wallet Car Dog
class Wallet:
    pass

a= 10
b= "dadasda"
wallet1 = Wallet()
type(a)
<class 'int'>
type(b)
<class 'str'>
type(wallet1)
<class '__main__.Wallet'>
wallet1
<__main__.Wallet object at 0x000001A5629F6A50>
class Dog:
    pass

class Car:
    pass

lada = Car()
bobik = Dog()
type(lada)
<class '__main__.Car'>
type(bobik)
<class '__main__.Dog'>



# Wallet Car Dog
# Wallet - id amount owner
class Wallet:
    def __init__(self, wid, wamount, wowner):
        pass

    
wallet1 = Wallet(2, 100, "vasya")
wallet1
<__main__.Wallet object at 0x000001A5629F6E40>
wallet1.wid
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    wallet1.wid
AttributeError: 'Wallet' object has no attribute 'wid'
class Wallet:
    def __init__(self, wid, wamount, wowner):
        self.wallet_id = wid
        self.wallet_amount = wamount
        self.wallet_owner = wowner

        
wallet1 = Wallet(2, 100, "vasya")
wallet1.wallet_id
2
wallet1.wallet_amount
100
wallet1.wallet_owner
'vasya'
wallet2 = Wallet(44, 10000, "petya")
wallet2.wallet_id
44
wallet1.wallet_id
2
wallet2.wallet_amount
10000
wallet2.wallet_owner
'petya'
# Wallet Car Dog

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        
Bobik = Dog("Bobik", 1)
Bobik.name
'Bobik'
Bobik.age
1
Дружок = Dog("Dryzhok", 0.5)
Дружок.name
'Dryzhok'
Дружок.
SyntaxError: invalid syntax
Дружок.age
0.5
Bobik.name
'Bobik'
Bobik.age
1

class User:
    def __init__(self , name, phone, email)
    
SyntaxError: expected ':'
class Client:
    def __init__(self , name, phone, email=None):
        self.name = name
        self.phone = phone
        self.email = email

        
client1 = Client("Dima", 12312313)
client2 = Client("Vasya", 123123, "sasdadasd@sad.com")
client1.name
'Dima'
client1.phone
12312313
client2.name
'Vasya'
client2.phone
123123
client2.email
'sasdadasd@sad.com'
type(client1)
<class '__main__.Client'>
type(client2)
<class '__main__.Client'>



storage = []
client_storage = []
n = 4
for i in range(1, n + 1):
    print("client number is :", i)
    name = input("name:")
    phone = input("phone:")
    email = input("email:")
    client = Client(name, phone, email)
    client_storage.append(client)

    
client number is : 1
name:vasia
phone:312354
email:
client number is : 2
name:Petya
phone:454656
email:asdasdasd@adad.com
client number is : 3
name:kate
phone:999
email:
client number is : 4
name:Sasha
phone:45645
email:sdfsfdsfsf@afas.com
client_storage
[<__main__.Client object at 0x000001A5629FFED0>, <__main__.Client object at 0x000001A562B2C050>, <__main__.Client object at 0x000001A562B2C190>, <__main__.Client object at 0x000001A562B2C2D0>]

def show_clients(clients):
    for client in clients:
        print("name:", client.name)
        print("phone:", client.phone)
        print("email:", client.email)
        print()
    print()

    
show_clients(client_storage)
name: vasia
phone: 312354
email: 

name: Petya
phone: 454656
email: asdasdasd@adad.com

name: kate
phone: 999
email: 

name: Sasha
phone: 45645
email: sdfsfdsfsf@afas.com





class Dog:
    class_variable = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age

        
Dog.class_variable
0
dog1 = Dog("dog", 1)
dog1.name
'dog'
dog1.
SyntaxError: invalid syntax
dog1.age
1
dog1.class_variable
0
dog1.name
'dog'
dog1.name = "Bobik"
dog1.name
'Bobik'
dog1.age = 10000
dog1.age
10000
Dog.class_variable = 10000
Dog.class_variable
10000
Dog.class_variable = 312
Dog.class_variable
312



class Task:
    counter = 1
    def __init__(self, name):
        self.task_id = Task.counter
        Task.counter += 1
        self.task_name = name
        self.task_status = False

        
t1 = Task("go")
t2 = Task("run")
t3 = Task("sleep")
print(t1.task_id, t1.task_name, t1.task_status)
1 go False
print(t2.task_id, t2.task_name, t2.task_status)
2 run False
print(t3.task_id, t3.task_name, t3.task_status)
3 sleep False
t4 = Task("sing")
print(t4.task_id, t4.task_name, t4.task_status)
4 sing False
t1.__dict__
{'task_id': 1, 'task_name': 'go', 'task_status': False}
Taks.__dict__
Traceback (most recent call last):
  File "<pyshell#172>", line 1, in <module>
    Taks.__dict__
NameError: name 'Taks' is not defined
s = Task()
Traceback (most recent call last):
  File "<pyshell#173>", line 1, in <module>
    s = Task()
TypeError: Task.__init__() missing 1 required positional argument: 'name'
class f:
    """asdadsadsadsadsadasd."""
    a = 9
    def __init__(self):
        pass

    
help(f)
Help on class f in module __main__:

class f(builtins.object)
 |  asdadsadsadsadsadasd.
 |
 |  Methods defined here:
 |
 |  __init__(self)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables
 |
 |  __weakref__
 |      list of weak references to the object
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  a = 9

f.__dict__
mappingproxy({'__module__': '__main__', '__firstlineno__': 1, '__doc__': 'asdadsadsadsadsadasd.', 'a': 9, '__init__': <function f.__init__ at 0x000001A562B11B20>, '__static_attributes__': (), '__dict__': <attribute '__dict__' of 'f' objects>, '__weakref__': <attribute '__weakref__' of 'f' objects>})
Task.__dict__
mappingproxy({'__module__': '__main__', '__firstlineno__': 1, 'counter': 5, '__init__': <function Task.__init__ at 0x000001A562B12160>, '__static_attributes__': ('task_id', 'task_name', 'task_status'), '__dict__': <attribute '__dict__' of 'Task' objects>, '__weakref__': <attribute '__weakref__' of 'Task' objects>, '__doc__': None})



class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hello(self):
        print(f"Hello! My name is {self.name}, and I'm{self.age} old!")

        
Cat.hello
<function Cat.hello at 0x000001A562B11DA0>
barsic = Cat("Barsik" , 3)
barsic.hello()
Hello! My name is Barsik, and I'm3 old!
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hello(self):
        print(f"Hello! My name is {self.name}, and I'm {self.age} old!")

        
barsic.name
'Barsik'

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hello(self):
        print(f"Hello! My name is {self.name}, and I'm {self.age} old!")
    def say(self, msg):
        print(f"{self.name} says: {msg}!")

        
barsic = Cat("Barsik" , 3)
barsic.hello()
Hello! My name is Barsik, and I'm 3 old!
barsic.say("Meow!")
Barsik says: Meow!!
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hello(self):
        print(f"Hello! My name is {self.name}, and I'm {self.age} old!")
    def say(self, msg):
        print(f"{self.name} says: {msg}!")
    def grow(self):
        self.age += 1


barsic = Cat("Barsik" , 3)
barsic.hello()
Hello! My name is Barsik, and I'm 3 old!
barsic.grow()
barsic.hello()
Hello! My name is Barsik, and I'm 4 old!
barsic.grow()
barsic.hello()
Hello! My name is Barsik, and I'm 5 old!




a = 1
li = [1,2,3,4]
a
1
li
[1, 2, 3, 4]
print(a, li)
1 [1, 2, 3, 4]
barsic
<__main__.Cat object at 0x000001A5629F6E40>
print(barsic)
<__main__.Cat object at 0x000001A5629F6E40>



a = 5
a
5
# __repr__
print(a)
5
# __str__
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hello(self):
        print(f"Hello! My name is {self.name}, and I'm {self.age} old!")
    def say(self, msg):
        print(f"{self.name} says: {msg}!")
    def grow(self):
        self.age += 1
    def __repr__(self):
        return f"cat info.\nname:{self.name}\nage:{self.age}"

    
barsic = Cat("Barsik" , 3)
barsic
cat info.
name:Barsik
age:3
print(barsic)
cat info.
name:Barsik
age:3
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hello(self):
        print(f"Hello! My name is {self.name}, and I'm {self.age} old!")
    def say(self, msg):
        print(f"{self.name} says: {msg}!")
    def grow(self):
        self.age += 1
    def __repr__(self):
        return f"cat info.\nname:{self.name}\nage:{self.age}"
    def __str__(self):
        return f"{self.name}|{self.age}"

    
barsic = Cat("Barsik" , 3)
barsic
cat info.
name:Barsik
age:3
print(barsic)
Barsik|3



help(Cat)
Help on class Cat in module __main__:

class Cat(builtins.object)
 |  Cat(name, age)
 |
 |  Methods defined here:
 |
 |  __init__(self, name, age)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  __repr__(self)
 |      Return repr(self).
 |
 |  __str__(self)
 |      Return str(self).
 |
 |  grow(self)
 |
 |  hello(self)
 |
 |  say(self, msg)
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables
 |
 |  __weakref__
 |      list of weak references to the object

help(int)
Help on class int in module builtins:

class int(object)
 |  int([x]) -> integer
 |  int(x, base=10) -> integer
 |
 |  Convert a number or string to an integer, or return 0 if no arguments
 |  are given.  If x is a number, return x.__int__().  For floating-point
 |  numbers, this truncates towards zero.
 |
 |  If x is not a number or if base is given, then x must be a string,
 |  bytes, or bytearray instance representing an integer literal in the
 |  given base.  The literal can be preceded by '+' or '-' and be surrounded
 |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
 |  Base 0 means to interpret the base from the string as an integer literal.
 |  >>> int('0b100', base=0)
 |  4
 |
 |  Built-in subclasses:
 |      bool
 |
 |  Methods defined here:
 |
 |  __abs__(self, /)
 |      abs(self)
 |
 |  __add__(self, value, /)
 |      Return self+value.
 |
 |  __and__(self, value, /)
 |      Return self&value.
 |
 |  __bool__(self, /)
 |      True if self else False
 |
 |  __ceil__(self, /)
 |      Ceiling of an Integral returns itself.
 |
 |  __divmod__(self, value, /)
 |      Return divmod(self, value).
 |
 |  __eq__(self, value, /)
 |      Return self==value.
 |
 |  __float__(self, /)
 |      float(self)
 |
 |  __floor__(self, /)
 |      Flooring an Integral returns itself.
 |
 |  __floordiv__(self, value, /)
 |      Return self//value.
 |
 |  __format__(self, format_spec, /)
 |      Convert to a string according to format_spec.
 |
 |  __ge__(self, value, /)
 |      Return self>=value.
 |
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |
 |  __getnewargs__(self, /)
 |
 |  __gt__(self, value, /)
 |      Return self>value.
 |
 |  __hash__(self, /)
 |      Return hash(self).
 |
 |  __index__(self, /)
 |      Return self converted to an integer, if self is suitable for use as an index into a list.
 |
 |  __int__(self, /)
 |      int(self)
 |
 |  __invert__(self, /)
 |      ~self
 |
 |  __le__(self, value, /)
 |      Return self<=value.
 |
 |  __lshift__(self, value, /)
 |      Return self<<value.
 |
 |  __lt__(self, value, /)
 |      Return self<value.
 |
 |  __mod__(self, value, /)
 |      Return self%value.
 |
 |  __mul__(self, value, /)
 |      Return self*value.
 |
 |  __ne__(self, value, /)
 |      Return self!=value.
 |
 |  __neg__(self, /)
 |      -self
 |
 |  __or__(self, value, /)
 |      Return self|value.
 |
 |  __pos__(self, /)
 |      +self
 |
 |  __pow__(self, value, mod=None, /)
 |      Return pow(self, value, mod).
 |
 |  __radd__(self, value, /)
 |      Return value+self.
 |
 |  __rand__(self, value, /)
 |      Return value&self.
 |
 |  __rdivmod__(self, value, /)
 |      Return divmod(value, self).
 |
 |  __repr__(self, /)
 |      Return repr(self).
 |
 |  __rfloordiv__(self, value, /)
 |      Return value//self.
 |
 |  __rlshift__(self, value, /)
 |      Return value<<self.
 |
 |  __rmod__(self, value, /)
 |      Return value%self.
 |
 |  __rmul__(self, value, /)
 |      Return value*self.
 |
 |  __ror__(self, value, /)
 |      Return value|self.
 |
 |  __round__(self, ndigits=<unrepresentable>, /)
 |      Rounding an Integral returns itself.
 |
 |      Rounding with an ndigits argument also returns an integer.
 |
 |  __rpow__(self, value, mod=None, /)
 |      Return pow(value, self, mod).
 |
 |  __rrshift__(self, value, /)
 |      Return value>>self.
 |
 |  __rshift__(self, value, /)
 |      Return self>>value.
 |
 |  __rsub__(self, value, /)
 |      Return value-self.
 |
 |  __rtruediv__(self, value, /)
 |      Return value/self.
 |
 |  __rxor__(self, value, /)
 |      Return value^self.
 |
 |  __sizeof__(self, /)
 |      Returns size in memory, in bytes.
 |
 |  __sub__(self, value, /)
 |      Return self-value.
 |
 |  __truediv__(self, value, /)
 |      Return self/value.
 |
 |  __trunc__(self, /)
 |      Truncating an Integral returns itself.
 |
 |  __xor__(self, value, /)
 |      Return self^value.
 |
 |  as_integer_ratio(self, /)
 |      Return a pair of integers, whose ratio is equal to the original int.
 |
 |      The ratio is in lowest terms and has a positive denominator.
 |
 |      >>> (10).as_integer_ratio()
 |      (10, 1)
 |      >>> (-10).as_integer_ratio()
 |      (-10, 1)
 |      >>> (0).as_integer_ratio()
 |      (0, 1)
 |
 |  bit_count(self, /)
 |      Number of ones in the binary representation of the absolute value of self.
 |
 |      Also known as the population count.
 |
 |      >>> bin(13)
 |      '0b1101'
 |      >>> (13).bit_count()
 |      3
 |
 |  bit_length(self, /)
 |      Number of bits necessary to represent self in binary.
 |
 |      >>> bin(37)
 |      '0b100101'
 |      >>> (37).bit_length()
 |      6
 |
 |  conjugate(self, /)
 |      Returns self, the complex conjugate of any int.
 |
 |  is_integer(self, /)
 |      Returns True. Exists for duck type compatibility with float.is_integer.
 |
 |  to_bytes(self, /, length=1, byteorder='big', *, signed=False)
 |      Return an array of bytes representing an integer.
 |
 |      length
 |        Length of bytes object to use.  An OverflowError is raised if the
 |        integer is not representable with the given number of bytes.  Default
 |        is length 1.
 |      byteorder
 |        The byte order used to represent the integer.  If byteorder is 'big',
 |        the most significant byte is at the beginning of the byte array.  If
 |        byteorder is 'little', the most significant byte is at the end of the
 |        byte array.  To request the native byte order of the host system, use
 |        sys.byteorder as the byte order value.  Default is to use 'big'.
 |      signed
 |        Determines whether two's complement is used to represent the integer.
 |        If signed is False and a negative integer is given, an OverflowError
 |        is raised.
 |
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |
 |  from_bytes(bytes, byteorder='big', *, signed=False)
 |      Return the integer represented by the given array of bytes.
 |
 |      bytes
 |        Holds the array of bytes to convert.  The argument must either
 |        support the buffer protocol or be an iterable object producing bytes.
 |        Bytes and bytearray are examples of built-in objects that support the
 |        buffer protocol.
 |      byteorder
 |        The byte order used to represent the integer.  If byteorder is 'big',
 |        the most significant byte is at the beginning of the byte array.  If
 |        byteorder is 'little', the most significant byte is at the end of the
 |        byte array.  To request the native byte order of the host system, use
 |        sys.byteorder as the byte order value.  Default is to use 'big'.
 |      signed
 |        Indicates whether two's complement is used to represent the integer.
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
 |  denominator
 |      the denominator of a rational number in lowest terms
 |
 |  imag
 |      the imaginary part of a complex number
 |
 |  numerator
 |      the numerator of a rational number in lowest terms
 |
 |  real
 |      the real part of a complex number


help(str)
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to 'utf-8'.
 |  errors defaults to 'strict'.
 |
 |  Methods defined here:
 |
 |  __add__(self, value, /)
 |      Return self+value.
 |
 |  __contains__(self, key, /)
 |      Return bool(key in self).
 |
 |  __eq__(self, value, /)
 |      Return self==value.
 |
 |  __format__(self, format_spec, /)
 |      Return a formatted version of the string as described by format_spec.
 |
 |  __ge__(self, value, /)
 |      Return self>=value.
 |
 |  __getitem__(self, key, /)
 |      Return self[key].
 |
 |  __getnewargs__(self, /)
 |
 |  __gt__(self, value, /)
 |      Return self>value.
 |
 |  __hash__(self, /)
 |      Return hash(self).
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
 |  __mod__(self, value, /)
 |      Return self%value.
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
 |  __rmod__(self, value, /)
 |      Return value%self.
 |
 |  __rmul__(self, value, /)
 |      Return value*self.
 |
 |  __sizeof__(self, /)
 |      Return the size of the string in memory, in bytes.
 |
 |  __str__(self, /)
 |      Return str(self).
 |
 |  capitalize(self, /)
 |      Return a capitalized version of the string.
 |
 |      More specifically, make the first character have upper case and the rest lower
 |      case.
 |
 |  casefold(self, /)
 |      Return a version of the string suitable for caseless comparisons.
 |
 |  center(self, width, fillchar=' ', /)
 |      Return a centered string of length width.
 |
 |      Padding is done using the specified fill character (default is a space).
 |
 |  count(self, sub[, start[, end]], /)
 |      Return the number of non-overlapping occurrences of substring sub in string S[start:end].
 |
 |      Optional arguments start and end are interpreted as in slice notation.
 |
 |  encode(self, /, encoding='utf-8', errors='strict')
 |      Encode the string using the codec registered for encoding.
 |
 |      encoding
 |        The encoding in which to encode the string.
 |      errors
 |        The error handling scheme to use for encoding errors.
 |        The default is 'strict' meaning that encoding errors raise a
 |        UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
 |        'xmlcharrefreplace' as well as any other name registered with
 |        codecs.register_error that can handle UnicodeEncodeErrors.
 |
 |  endswith(self, suffix[, start[, end]], /)
 |      Return True if the string ends with the specified suffix, False otherwise.
 |
 |      suffix
 |        A string or a tuple of strings to try.
 |      start
 |        Optional start position. Default: start of the string.
 |      end
 |        Optional stop position. Default: end of the string.
 |
 |  expandtabs(self, /, tabsize=8)
 |      Return a copy where all tab characters are expanded using spaces.
 |
 |      If tabsize is not given, a tab size of 8 characters is assumed.
 |
 |  find(self, sub[, start[, end]], /)
 |      Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end].
 |
 |      Optional arguments start and end are interpreted as in slice notation.
 |      Return -1 on failure.
 |
 |  format(self, /, *args, **kwargs)
 |      Return a formatted version of the string, using substitutions from args and kwargs.
 |      The substitutions are identified by braces ('{' and '}').
 |
 |  format_map(self, mapping, /)
 |      Return a formatted version of the string, using substitutions from mapping.
 |      The substitutions are identified by braces ('{' and '}').
 |
 |  index(self, sub[, start[, end]], /)
 |      Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end].
 |
 |      Optional arguments start and end are interpreted as in slice notation.
 |      Raises ValueError when the substring is not found.
 |
 |  isalnum(self, /)
 |      Return True if the string is an alpha-numeric string, False otherwise.
 |
 |      A string is alpha-numeric if all characters in the string are alpha-numeric and
 |      there is at least one character in the string.
 |
 |  isalpha(self, /)
 |      Return True if the string is an alphabetic string, False otherwise.
 |
 |      A string is alphabetic if all characters in the string are alphabetic and there
 |      is at least one character in the string.
 |
 |  isascii(self, /)
 |      Return True if all characters in the string are ASCII, False otherwise.
 |
 |      ASCII characters have code points in the range U+0000-U+007F.
 |      Empty string is ASCII too.
 |
 |  isdecimal(self, /)
 |      Return True if the string is a decimal string, False otherwise.
 |
 |      A string is a decimal string if all characters in the string are decimal and
 |      there is at least one character in the string.
 |
 |  isdigit(self, /)
 |      Return True if the string is a digit string, False otherwise.
 |
 |      A string is a digit string if all characters in the string are digits and there
 |      is at least one character in the string.
 |
 |  isidentifier(self, /)
 |      Return True if the string is a valid Python identifier, False otherwise.
 |
 |      Call keyword.iskeyword(s) to test whether string s is a reserved identifier,
 |      such as "def" or "class".
 |
 |  islower(self, /)
 |      Return True if the string is a lowercase string, False otherwise.
 |
 |      A string is lowercase if all cased characters in the string are lowercase and
 |      there is at least one cased character in the string.
 |
 |  isnumeric(self, /)
 |      Return True if the string is a numeric string, False otherwise.
 |
 |      A string is numeric if all characters in the string are numeric and there is at
 |      least one character in the string.
 |
 |  isprintable(self, /)
 |      Return True if the string is printable, False otherwise.
 |
 |      A string is printable if all of its characters are considered printable in
 |      repr() or if it is empty.
 |
 |  isspace(self, /)
 |      Return True if the string is a whitespace string, False otherwise.
 |
 |      A string is whitespace if all characters in the string are whitespace and there
 |      is at least one character in the string.
 |
 |  istitle(self, /)
 |      Return True if the string is a title-cased string, False otherwise.
 |
 |      In a title-cased string, upper- and title-case characters may only
 |      follow uncased characters and lowercase characters only cased ones.
 |
 |  isupper(self, /)
 |      Return True if the string is an uppercase string, False otherwise.
 |
 |      A string is uppercase if all cased characters in the string are uppercase and
 |      there is at least one cased character in the string.
 |
 |  join(self, iterable, /)
 |      Concatenate any number of strings.
 |
 |      The string whose method is called is inserted in between each given string.
 |      The result is returned as a new string.
 |
 |      Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
 |
 |  ljust(self, width, fillchar=' ', /)
 |      Return a left-justified string of length width.
 |
 |      Padding is done using the specified fill character (default is a space).
 |
 |  lower(self, /)
 |      Return a copy of the string converted to lowercase.
 |
 |  lstrip(self, chars=None, /)
 |      Return a copy of the string with leading whitespace removed.
 |
 |      If chars is given and not None, remove characters in chars instead.
 |
 |  partition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |
 |      This will search for the separator in the string.  If the separator is found,
 |      returns a 3-tuple containing the part before the separator, the separator
 |      itself, and the part after it.
 |
 |      If the separator is not found, returns a 3-tuple containing the original string
 |      and two empty strings.
 |
 |  removeprefix(self, prefix, /)
 |      Return a str with the given prefix string removed if present.
 |
 |      If the string starts with the prefix string, return string[len(prefix):].
 |      Otherwise, return a copy of the original string.
 |
 |  removesuffix(self, suffix, /)
 |      Return a str with the given suffix string removed if present.
 |
 |      If the string ends with the suffix string and that suffix is not empty,
 |      return string[:-len(suffix)]. Otherwise, return a copy of the original
 |      string.
 |
 |  replace(self, old, new, /, count=-1)
 |      Return a copy with all occurrences of substring old replaced by new.
 |
 |        count
 |          Maximum number of occurrences to replace.
 |          -1 (the default value) means replace all occurrences.
 |
 |      If the optional argument count is given, only the first count occurrences are
 |      replaced.
 |
 |  rfind(self, sub[, start[, end]], /)
 |      Return the highest index in S where substring sub is found, such that sub is contained within S[start:end].
 |
 |      Optional arguments start and end are interpreted as in slice notation.
 |      Return -1 on failure.
 |
 |  rindex(self, sub[, start[, end]], /)
 |      Return the highest index in S where substring sub is found, such that sub is contained within S[start:end].
 |
 |      Optional arguments start and end are interpreted as in slice notation.
 |      Raises ValueError when the substring is not found.
 |
 |  rjust(self, width, fillchar=' ', /)
 |      Return a right-justified string of length width.
 |
 |      Padding is done using the specified fill character (default is a space).
 |
 |  rpartition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |
 |      This will search for the separator in the string, starting at the end. If
 |      the separator is found, returns a 3-tuple containing the part before the
 |      separator, the separator itself, and the part after it.
 |
 |      If the separator is not found, returns a 3-tuple containing two empty strings
 |      and the original string.
 |
 |  rsplit(self, /, sep=None, maxsplit=-1)
 |      Return a list of the substrings in the string, using sep as the separator string.
 |
 |        sep
 |          The separator used to split the string.
 |
 |          When set to None (the default value), will split on any whitespace
 |          character (including \n \r \t \f and spaces) and will discard
 |          empty strings from the result.
 |        maxsplit
 |          Maximum number of splits.
 |          -1 (the default value) means no limit.
 |
 |      Splitting starts at the end of the string and works to the front.
 |
 |  rstrip(self, chars=None, /)
 |      Return a copy of the string with trailing whitespace removed.
 |
 |      If chars is given and not None, remove characters in chars instead.
 |
 |  split(self, /, sep=None, maxsplit=-1)
 |      Return a list of the substrings in the string, using sep as the separator string.
 |
 |        sep
 |          The separator used to split the string.
 |
 |          When set to None (the default value), will split on any whitespace
 |          character (including \n \r \t \f and spaces) and will discard
 |          empty strings from the result.
 |        maxsplit
 |          Maximum number of splits.
 |          -1 (the default value) means no limit.
 |
 |      Splitting starts at the front of the string and works to the end.
 |
 |      Note, str.split() is mainly useful for data that has been intentionally
 |      delimited.  With natural text that includes punctuation, consider using
 |      the regular expression module.
 |
 |  splitlines(self, /, keepends=False)
 |      Return a list of the lines in the string, breaking at line boundaries.
 |
 |      Line breaks are not included in the resulting list unless keepends is given and
 |      true.
 |
 |  startswith(self, prefix[, start[, end]], /)
 |      Return True if the string starts with the specified prefix, False otherwise.
 |
 |      prefix
 |        A string or a tuple of strings to try.
 |      start
 |        Optional start position. Default: start of the string.
 |      end
 |        Optional stop position. Default: end of the string.
 |
 |  strip(self, chars=None, /)
 |      Return a copy of the string with leading and trailing whitespace removed.
 |
 |      If chars is given and not None, remove characters in chars instead.
 |
 |  swapcase(self, /)
 |      Convert uppercase characters to lowercase and lowercase characters to uppercase.
 |
 |  title(self, /)
 |      Return a version of the string where each word is titlecased.
 |
 |      More specifically, words start with uppercased characters and all remaining
 |      cased characters have lower case.
 |
 |  translate(self, table, /)
 |      Replace each character in the string using the given translation table.
 |
 |        table
 |          Translation table, which must be a mapping of Unicode ordinals to
 |          Unicode ordinals, strings, or None.
 |
 |      The table must implement lookup/indexing via __getitem__, for instance a
 |      dictionary or list.  If this operation raises LookupError, the character is
 |      left untouched.  Characters mapped to None are deleted.
 |
 |  upper(self, /)
 |      Return a copy of the string converted to uppercase.
 |
 |  zfill(self, width, /)
 |      Pad a numeric string with zeros on the left, to fill a field of the given width.
 |
 |      The string is never truncated.
 |
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |
 |  __new__(*args, **kwargs)
 |      Create and return a new object.  See help(type) for accurate signature.
 |
 |  maketrans(x, y=<unrepresentable>, z=<unrepresentable>, /)
 |      Return a translation table usable for str.translate().
 |
 |      If there is only one argument, it must be a dictionary mapping Unicode
 |      ordinals (integers) or characters to Unicode ordinals, strings or None.
 |      Character keys will be then converted to ordinals.
 |      If there are two arguments, they must be strings of equal length, and
 |      in the resulting dictionary, each character in x will be mapped to the
 |      character at the same position in y. If there is a third argument, it
 |      must be a string, whose characters will be mapped to None in the result.




class Dog:
    pass

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hello(self):
        print(f"Hello! My name is {self.name}, and I'm {self.age} old!")
    def say(self, msg):
        print(f"{self.name} says: {msg}!")
    def grow(self):
        self.age += 1
    def __repr__(self):
        return f"cat info.\nname:{self.name}\nage:{self.age}"
    def __str__(self):
        return f"{self.name}|{self.age}"

    
d = Dog()
d
<__main__.Dog object at 0x000001A5629F7620>
Dog.__bases__
(<class 'object'>,)
Cat.__bases__
(<class 'object'>,)
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hello(self):
        print(f"Hello! My name is {self.name}, and I'm {self.age} old!")
    def say(self, msg):
        print(f"{self.name} says: {msg}!")
    def grow(self):
        self.age += 1
    def __repr__(self):
        return f"cat info.\nname:{self.name}\nage:{self.age}"
    def __str__(self):
        return f"{self.name}|{self.age}"

    
# swimming_cat
class SwimmingCat(Cat):
    def swim(self):
        print("I can swim!")

   
sadik = SwimmingCat("sadik", 2)

sadik.name
'sadik'
sadik
cat info.
name:sadik
age:2
print(sadik)
sadik|2
sadik.swim()
I can swim!
type(sadik)
<class '__main__.SwimmingCat'>
sadik.grow
<bound method Cat.grow of cat info.
name:sadik
age:2>
sadik.hello()
Hello! My name is sadik, and I'm 2 old!
class SwimmingCat(Cat):
    def swim(self):
        print("I can swim!")
    def __str__(self):
        return f"SwimmingCat:{self.name}|{self.age}"

    
sadik = SwimmingCat("sadik", 2)
print(sadik)
SwimmingCat:sadik|2
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hello(self):
        print(f"Hello! My name is {self.name}, and I'm {self.age} old!")
    def say(self, msg):
        print(f"{self.name} says: {msg}!")
    def grow(self):
        self.age += 1
    def __repr__(self):
        return f"cat info.\nname:{self.name}\nage:{self.age}"
    def __str__(self):
        return f"{self.name}|{self.age}"

    
class SwimmingCat(Cat):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    def swim(self):
        print("I can swim!")
    def __str__(self):
        return f"SwimmingCat:{self.name}|{self.age}"

    
sadik = SwimmingCat("sadik", 2, "RED")
sadik.color()
Traceback (most recent call last):
  File "<pyshell#295>", line 1, in <module>
    sadik.color()
TypeError: 'str' object is not callable
sadik.__dict__
{'name': 'sadik', 'age': 2, 'color': 'RED'}
class SwimmingCat(Cat):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    def swim(self):
        print("I can swim!")
    def hello(self):
        super().hello()
        print(f"my color is {self.color}")
    def __str__(self):
        return f"SwimmingCat:{self.name}|{self.age}"

    
sadik = SwimmingCat("sadik", 2, "RED")
sadik.hello()
Hello! My name is sadik, and I'm 2 old!
my color is RED
# class
# class Name (от кого наслудемся через запятую):
# super().__init__(...) - это позволит дернуть родительский конструктор
# super().hello()  - чтобы вызвать метод из родителя


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hello(self):
        print(f"Hello! My name is {self.name}, and I'm {self.age} old!")
    def __str__(self):
        return f"{self.name}|{self.age}"

    
c1 =Cat("jojo", 1)
c1.hello()
Hello! My name is jojo, and I'm 1 old!
c1.name
'jojo'
c1.name = "NoName"
c1.name
'NoName'
c1.hello()
Hello! My name is NoName, and I'm 1 old!
class Cat:
    def __init__(self, name, age):
        self.__name = name
        self.age = age
    def hello(self):
        print(f"Hello! My name is {self.__name}, and I'm {self.age} old!")
    def __str__(self):
        return f"{self.__name}|{self.age}"

...     
>>> c1 =Cat("jojo", 1)
>>> c1.name
Traceback (most recent call last):
  File "<pyshell#318>", line 1, in <module>
    c1.name
AttributeError: 'Cat' object has no attribute 'name'
>>> c1.hello()
Hello! My name is jojo, and I'm 1 old!
>>> c1.__dict__
{'_Cat__name': 'jojo', 'age': 1}
>>> class Cat:
...     def __init__(self, name, age):
...         self.__name = name
...         self.age = age
...     def hello(self):
...         print(f"Hello! My name is {self.__name}, and I'm {self.age} old!")
...     def __str__(self):
...         return f"{self.__name}|{self.age}"
...     def change_name(self, name):
...         self.__name = name
... 
...         
>>> c1 =Cat("jojo", 1)
>>> c1.__name
Traceback (most recent call last):
  File "<pyshell#326>", line 1, in <module>
    c1.__name
AttributeError: 'Cat' object has no attribute '__name'
>>> c1.name
Traceback (most recent call last):
  File "<pyshell#327>", line 1, in <module>
    c1.name
AttributeError: 'Cat' object has no attribute 'name'
>>> c1.hello()
Hello! My name is jojo, and I'm 1 old!
>>> c1.change_name("JOJO")
>>> c1.hello()
Hello! My name is JOJO, and I'm 1 old!
