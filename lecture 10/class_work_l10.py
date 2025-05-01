Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
12123132 + 546465
12669597
1213 * 5456465
6618692045
li = [1,2,3,4,5,6]
li
[1, 2, 3, 4, 5, 6]
print(li)
[1, 2, 3, 4, 5, 6]
li[1]
2
li[-1]
6
di = {1:11, 2:22}
di[1]
11
del di
di
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    di
NameError: name 'di' is not defined


try:
    print(di)
except NameError:
    print("aasdasd")

    
aasdasd
try:
    print(di)
except NameError:
    print("aasdasd")
    raise

aasdasd
Traceback (most recent call last):
  File "<pyshell#21>", line 2, in <module>
    print(di)
NameError: name 'di' is not defined
try:
    asdsada
except:
    print(asdasd)
except NameError:
    print(123)
    
SyntaxError: default 'except:' must be last

try:
    asdsada
except:
    print(asdasd)
except:
    print(asdasd)
    
SyntaxError: default 'except:' must be last






























try:
    asdsada
except NameError:
    print(123)
except:
    print(asdasd)

    
123









# Car
# vin volume body_type
class Car:
    def __init__(self, vin, volume, body_type):
        self.vin = vin
        self.volume = volume
        self.body_type = body_type
    def __repr__(self):
        return f"Car({self.vin}, {self.volume}, {self.body_type})"

    
lada1 = Car("12312345", 1.67, "hatchback")
lada1
Car(12312345, 1.67, hatchback)
lada1.__dict__
{'vin': '12312345', 'volume': 1.67, 'body_type': 'hatchback'}
di = lada1.__dict__
di
{'vin': '12312345', 'volume': 1.67, 'body_type': 'hatchback'}
type(di)
<class 'dict'>
di.get("vin")
'12312345'
di.get("volume")
1.67
lada1.vin
'12312345'
lada2 = Car("4564546546", 1.9, "sedan")
lada2
Car(4564546546, 1.9, sedan)
li = [lada1, lada2]
for car_inst in li:
    print(car_inst.vin)
    print(car_inst.volume)
    print(car_inst.body_type)

    
12312345
1.67
hatchback
4564546546
1.9
sedan
for car_inst in li:
    print()
    for k, v in car_inst.__dict__.items():
        print(k, ":", v)

        

vin : 12312345
volume : 1.67
body_type : hatchback

vin : 4564546546
volume : 1.9
body_type : sedan
class Car:
    def __init__(self, vin, volume, body_type):
        self.vin = vin
        self.volume = volume
        self.body_type = body_type
    def __repr__(self):
        return f"Car({self.vin}, {self.volume}, {self.body_type})"body_type : sedan
    
SyntaxError: invalid syntax
class Car:
    def __init__(sddsfdsf, vin, volume, body_type):
        sddsfdsf.vin = vin
        sddsfdsf.volume = volume
        sddsfdsf.body_type = body_type
    def __repr__(self):
        return f"Car({sddsfdsf.vin}, {sddsfdsf.volume}, {sddsfdsf.body_type})"

    
lada2 = Car("4564546546", 1.9, "sedan")
class Car:
    def __init__(sddsfdsf, vin, volume, body_type):
        sddsfdsf.vin = vin
        sddsfdsf.volume = volume
        sddsfdsf.body_type = body_type
    def __repr__(sddsfdsf):
        return f"Car({sddsfdsf.vin}, {sddsfdsf.volume}, {sddsfdsf.body_type})"

    
lada2 = Car("4564546546", 1.9, "sedan")
lada2
Car(4564546546, 1.9, sedan)
class Car:
    def __init__(self, vin, volume, body_type):
        self.vin = vin
        self.volume = volume
        self.body_type = body_type
    def __repr__(self):
        return f"Car({self.vin}, {self.volume}, {self.body_type})"

    
lada2 = Car("4564546546", 1.9, "sedan")
lada2
Car(4564546546, 1.9, sedan)
lada2.body_type = "coupe"
lada2
Car(4564546546, 1.9, coupe)
lada2.new_var = 123123123
lada2
Car(4564546546, 1.9, coupe)
lada2.__dict__
{'vin': '4564546546', 'volume': 1.9, 'body_type': 'coupe', 'new_var': 123123123}
Car.__dict__
mappingproxy({'__module__': '__main__', '__firstlineno__': 1, '__init__': <function Car.__init__ at 0x000001BF38F51F80>, '__repr__': <function Car.__repr__ at 0x000001BF38F52020>, '__static_attributes__': ('body_type', 'vin', 'volume'), '__dict__': <attribute '__dict__' of 'Car' objects>, '__weakref__': <attribute '__weakref__' of 'Car' objects>, '__doc__': None})
class S:
    pass

class Car:
    def __init__(self, vin, volume, body_type):
        self.vin = vin
        self.volume = volume
        self.body_type = body_type
    def __repr__(self):
        return f"Car({self.vin}, {self.volume}, {self.body_type})"
    def move(self):
        print("move")
    def turn(self, direc):
        print("turn", direc)
    def xtop(self):
        print("stop")

        
class SportCar(Car):
    def __init__(self,vin, volume, body_type, speed_limit = 270, max_speed = 300):
        super().__init__(vin, volume, body_type)
        self.speed_limit = speed_limit
        self.max_speed = max_speed
    def __repr__(self):
        super().__repr__()
        return f"SportCar({self.speed_limit}, {self.max_speed})"
    def race(self):
        print(f"race with {self.max_speed} km\h")

        
renault = SportCar("11111111", 3.5, "coupe")
renault
SportCar(270, 300)
print(renault)
SportCar(270, 300)
class SportCar(Car):
    def __init__(self,vin, volume, body_type, speed_limit = 270, max_speed = 300):
        super().__init__(vin, volume, body_type)
        self.speed_limit = speed_limit
        self.max_speed = max_speed
    def __repr__(self):
        super().__repr__()
        return  super().__repr__() +"\n" + f"SportCar({self.speed_limit}, {self.max_speed})"
    def race(self):
        print(f"race with {self.max_speed} km\h")

        
renault = SportCar("11111111", 3.5, "coupe")
renault
Car(11111111, 3.5, coupe)
SportCar(270, 300)
renault.__dict__
{'vin': '11111111', 'volume': 3.5, 'body_type': 'coupe', 'speed_limit': 270, 'max_speed': 300}
renault.move()
move
renault.xtop()
stop
renault.race()
race with 300 km\h




class Dog:
    def say(self , msg):
        print(msg)

        
class Cat:
    def say(self , msg):
        print(msg)

        
class Bird:
    def say(self , msg):
        print(msg)

        
d, c, b = Dog(), Cat(), Bird()
d.say("dog"), c.say("cat"), b.say("kria")
dog
cat
kria
(None, None, None)
i, f, s = 12, 3.4, "sad"
i *3
36
f * 3
10.2
s * 3
'sadsadsad'




# Stack

class Stack:
    def __init__(self):
        self.__stack = []
        print("stack sozdan yspeshno")
    def push(self, value):
        self.__stack.append(value)
        print(value, "dobavleno")
    def pop(self):
        print(self.__stack.pop(), "yspeshno delete.")

        
s1 = Stack()
stack sozdan yspeshno
s1.push(4)
4 dobavleno
s1.push(44)
44 dobavleno
s1.push(3)
3 dobavleno
s1.push(2)
2 dobavleno
s1.__dict__
{'_Stack__stack': [4, 44, 3, 2]}
s1.pop()
2 yspeshno delete.
s1.pop()
3 yspeshno delete.
s1.pop()
44 yspeshno delete.
s1.pop()
4 yspeshno delete.
s1.pop()
Traceback (most recent call last):
  File "<pyshell#179>", line 1, in <module>
    s1.pop()
  File "<pyshell#168>", line 9, in pop
    print(self.__stack.pop(), "yspeshno delete.")
IndexError: pop from empty list
class Stack:
    def __init__(self):
        self.__stack = []
        print("stack sozdan yspeshno")
    def push(self, value):
        self.__stack.append(value)
        print(value, "dobavleno")
    def pop(self):
        print(self.__stack.pop(), "yspeshno delete.")
    def state(self):
        print("tekyshee sostoania")
        print(self.__stack)

        
s1 = Stack()
stack sozdan yspeshno
s1.push(555)
555 dobavleno
s1.push(55)
55 dobavleno
s1.push(5)
5 dobavleno
s1.state
<bound method Stack.state of <__main__.Stack object at 0x000001BF38E3B4D0>>
s1.state()
tekyshee sostoania
[555, 55, 5]
s1.pop()
5 yspeshno delete.
s1.pop()
55 yspeshno delete.
s1.pop()
555 yspeshno delete.
class Stack:
    def __init__(self):
        self.__stack = []
        print("stack sozdan yspeshno")
    def push(self, value):
        self.__stack.append(value)
        print(value, "dobavleno")
    def pop(self):
        try:
            print(self.__stack.pop(), "yspeshno delete.")
        except:
            print("stack yze pysto")
    def state(self):
        print("tekyshee sostoania")
        print(self.__stack)

        
s1 = Stack()
stack sozdan yspeshno
s1.state()
tekyshee sostoania
[]
s1.pop()
stack yze pysto
class Stack:
    def __init__(self):
        self.__stack = []
        print("stack sozdan yspeshno")
    def push(self, value):
        self.__stack.append(value)
        print(value, "dobavleno")
    def pop(self):
        try:
            print(self.__stack.pop(), "yspeshno delete.")
        except:
            print("stack yze pysto")
    def state(self):
        print("tekyshee sostoania")
        print(self.__stack)

        
class AddStackValues(Stack):
    def __init__(self):
        super().__init__()
        self.__summa = 0
    def push(self, value):
        super().push(value)
        self.__summa += value
    def get_summa(self):
        print(self.__summa)

        
s2 = AddStackValues()
stack sozdan yspeshno
s2.get_summa()
0
s2.state()
tekyshee sostoania
[]
s2.push(3)
3 dobavleno
s2.state()
tekyshee sostoania
[3]
s2.get_summa()
3
s2.push(33)
33 dobavleno
s2.push(5)
5 dobavleno
s2.state()
tekyshee sostoania
[3, 33, 5]
s2.get_summa()
41


a = 10
b = 15
a + b
25
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


a = 10
b = 15
a + b
25
a.__add__(b)
25
c, d = 3.13, 5.7
c +d
8.83
c.__add__(d)
8.83
help(float)
Help on class float in module builtins:

class float(object)
 |  float(x=0, /)
 |
 |  Convert a string or number to a floating-point number, if possible.
 |
 |  Methods defined here:
 |
 |  __abs__(self, /)
 |      abs(self)
 |
 |  __add__(self, value, /)
 |      Return self+value.
 |
 |  __bool__(self, /)
 |      True if self else False
 |
 |  __ceil__(self, /)
 |      Return the ceiling as an Integral.
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
 |      Return the floor as an Integral.
 |
 |  __floordiv__(self, value, /)
 |      Return self//value.
 |
 |  __format__(self, format_spec, /)
 |      Formats the float according to format_spec.
 |
 |  __ge__(self, value, /)
 |      Return self>=value.
 |
 |  __getnewargs__(self, /)
 |
 |  __gt__(self, value, /)
 |      Return self>value.
 |
 |  __hash__(self, /)
 |      Return hash(self).
 |
 |  __int__(self, /)
 |      int(self)
 |
 |  __le__(self, value, /)
 |      Return self<=value.
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
 |  __pos__(self, /)
 |      +self
 |
 |  __pow__(self, value, mod=None, /)
 |      Return pow(self, value, mod).
 |
 |  __radd__(self, value, /)
 |      Return value+self.
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
 |  __rmod__(self, value, /)
 |      Return value%self.
 |
 |  __rmul__(self, value, /)
 |      Return value*self.
 |
 |  __round__(self, ndigits=None, /)
 |      Return the Integral closest to x, rounding half toward even.
 |
 |      When an argument is passed, work like built-in round(x, ndigits).
 |
 |  __rpow__(self, value, mod=None, /)
 |      Return pow(value, self, mod).
 |
 |  __rsub__(self, value, /)
 |      Return value-self.
 |
 |  __rtruediv__(self, value, /)
 |      Return value/self.
 |
 |  __sub__(self, value, /)
 |      Return self-value.
 |
 |  __truediv__(self, value, /)
 |      Return self/value.
 |
 |  __trunc__(self, /)
 |      Return the Integral closest to x between 0 and x.
 |
 |  as_integer_ratio(self, /)
 |      Return a pair of integers, whose ratio is exactly equal to the original float.
 |
 |      The ratio is in lowest terms and has a positive denominator.  Raise
 |      OverflowError on infinities and a ValueError on NaNs.
 |
 |      >>> (10.0).as_integer_ratio()
 |      (10, 1)
 |      >>> (0.0).as_integer_ratio()
 |      (0, 1)
 |      >>> (-.25).as_integer_ratio()
 |      (-1, 4)
 |
 |  conjugate(self, /)
 |      Return self, the complex conjugate of any float.
 |
 |  hex(self, /)
 |      Return a hexadecimal representation of a floating-point number.
 |
 |      >>> (-0.1).hex()
 |      '-0x1.999999999999ap-4'
 |      >>> 3.14159.hex()
 |      '0x1.921f9f01b866ep+1'
 |
 |  is_integer(self, /)
 |      Return True if the float is an integer.
 |
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |
 |  __getformat__(typestr, /)
 |      You probably don't want to use this function.
 |
 |        typestr
 |          Must be 'double' or 'float'.
 |
 |      It exists mainly to be used in Python's test suite.
 |
 |      This function returns whichever of 'unknown', 'IEEE, big-endian' or 'IEEE,
 |      little-endian' best describes the format of floating-point numbers used by the
 |      C type named by typestr.
 |
 |  fromhex(string, /)
 |      Create a floating-point number from a hexadecimal string.
 |
 |      >>> float.fromhex('0x1.ffffp10')
 |      2047.984375
 |      >>> float.fromhex('-0x1p-1074')
 |      -5e-324
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
 |  imag
 |      the imaginary part of a complex number
 |
 |  real
 |      the real part of a complex number



class Dog:
    def __init__(self, number):
        self.number = number
    def __add__(self, dog_inst):
        return self.number + dog_inst.number

    
d1, d2 = Dog(4), Dog(6)
d1.__add__(d2)
10
d1 + d2
10
class Dog:
    def __init__(self, name, age, color, salary):
        self.name = name
        self.age = age
        self.color = color
        self.salary = salary

        
d1, d2 = Dog("Jo", 4, "red", 100), Dog("Jojo", 1, "blue", 1000)
d1 + d2
Traceback (most recent call last):
  File "<pyshell#249>", line 1, in <module>
    d1 + d2
TypeError: unsupported operand type(s) for +: 'Dog' and 'Dog'
class Dog:
    def __init__(self, name, age, color, salary):
        self.name = name
        self.age = age
        self.color = color
        self.salary = salary
    def __add__(self, next_dog):
        return self.salary + next_dog.salary

    
d1, d2 = Dog("Jo", 4, "red", 100), Dog("Jojo", 1, "blue", 1000)
d1 + d2
1100
len
<built-in function len>
class Dog:
    def __init__(self, name, age, color, salary):
        self.name = name
        self.age = age
        self.color = color
        self.salary = salary
    def __add__(self, next_dog):
        return self.salary + next_dog.salary
    def __len__(self):
        return self.age

    
d1, d2 = Dog("Jo", 4, "red", 100), Dog("Jojo", 1, "blue", 1000)
d1 + d2
1100
len(d1)
4
len(d2)
1
class Dog:
    def __init__(self, name, age, color, salary):
        self.name = name
        self.age = age
        self.color = color
        self.salary = salary
    def __add__(self, next_dog):
        return self.salary + next_dog.salary
    def __sub__(self, next_dog):
        return self.salary - next_dog.salary
    def __len__(self):
        return self.age

    
d1, d2 = Dog("Jo", 4, "red", 100), Dog("Jojo", 1, "blue", 1000)
d1 + d2
1100
d1 - d2
-900
len(d2)
1
# __eq__()
# __ne__()
# __eq__() ==
# __ne__() !=
class Dog:
    def __init__(self, name, age, color, salary):
        self.name = name
        self.age = age
        self.color = color
        self.salary = salary
    def __add__(self, next_dog):
        return self.salary + next_dog.salary
    def __sub__(self, next_dog):
        return self.salary - next_dog.salary
    def __len__(self):
        return self.age
    def __eq__(self, next_dog):
        return self.name == next_dog.name
    def __ne__(self, next_dog):
        return self.name != next_dog.name

    
d1, d2 = Dog("Jo", 4, "red", 100), Dog("Jojo", 1, "blue", 1000)
d1 + d2
1100
d1 - d2
-900
d1 == d2
False
d1 != d2
True
class Dog:
    def __init__(self, name, age, color, salary):
        self.name = name
        self.age = age
        self.color = color
        self.salary = salary
    def __add__(self, next_dog):
        return self.salary + next_dog.salary
    def __sub__(self, next_dog):
        return self.salary - next_dog.salary
    def __len__(self):
        return self.age
    def __eq__(self, next_dog):
        return self.name == next_dog.name
    def __ne__(self, next_dog):
        return self.name != next_dog.name
    def __pow__(self, value):
        return self.age ** value
    def __mul__(self, next_dog):
        return self.age * next_dog.age

    
d1 + d2
1100
len(d1)
4
d1 ** 2
Traceback (most recent call last):
  File "<pyshell#293>", line 1, in <module>
    d1 ** 2
TypeError: unsupported operand type(s) for ** or pow(): 'Dog' and 'int'
d1, d2 = Dog("Jo", 4, "red", 100), Dog("Jojo", 1, "blue", 1000)
d1 ** 2
16
d2 ** 3
1
d1 * d2
4


return
SyntaxError: 'return' outside function
>>> if True:
...     return 123
SyntaxError: 'return' outside function
>>> for i in range(10):
...     return True
SyntaxError: 'return' outside function
>>> x = 0
>>> for i in range (10):
...     x += 1
... print(x)
SyntaxError: invalid syntax
>>> for i in range (10):
...     x += 1
... 
...     
>>> print(x)
10
>>> for i in range (10):
...     for j in range(1, 10, 1):
...         x += 1
... 
...         
>>> print(x)
100
>>> x = 0
>>> for i in range (10):
...     for j in range(1, 10, 1):
...         x += 1
... 
...         
>>> print(x)
90
>>> def func(num):
...     while num>0:
...         num = num - 1
... 
...         
>>> num = 3
>>> func(num)
>>> print(num)
3
