Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
1+1
2
2*3
6
li = [1,2,3,4,5]
li
[1, 2, 3, 4, 5]
li[1]
2
print(li)
[1, 2, 3, 4, 5]
se = {1,2,3,4,5,6}
di = {1:2, 2:22}
di[2]
22
di
{1: 2, 2: 22}
se
{1, 2, 3, 4, 5, 6}
4 in se
True



# user
class User:
    def __init__(self, n, a):
        self.name = n
        self.age = a
    def __repr__(self):
        return f"User({self.name}, {self.age})"

    
u1 = User("Vasia", 77)
u1
User(Vasia, 77)
u1.name
'Vasia'
u1.age
77
u1.age = 99
u1
User(Vasia, 99)
class User:
    user_counter = 0
    def __init__(self, n, a):
        self.name = n
        self.age = a
        User.user_counter += 1
    def __repr__(self):
        return f"User({self.name}, {self.age})"
    @classmethod
    def get_u_counter(cls):
        return f"User.user_counter = {cls.user_counter}."

    
User.get_u_counter()
'User.user_counter = 0.'
u1 = User("Vasia", 77)
User.get_u_counter()
'User.user_counter = 1.'
u2 = User("Vasia", 77)
u3 = User("Vasia", 77)
User.get_u_counter()
'User.user_counter = 3.'

class User:
    user_counter = 0
    def __init__(self, n, a):
        self.name = n
        self.age = a
        User.user_counter += 1
    def __repr__(self):
        return f"User({self.name}, {self.age})"
    @classmethod
    def get_u_counter(cls):
        return f"User.user_counter = {cls.user_counter}."
    @classmethod
    def job(cls):
        return cls.user_counter ** 2 / 2

    
u1 = User("Vasia", 77)
User.get_u_counter()
'User.user_counter = 1.'
User.job()
0.5
class User:
    user_counter = 0
    def __init__(self, n, a):
        self.name = n
        self.age = a
        User.user_counter += 1
    def __repr__(self):
        return f"User({self.name}, {self.age})"
    @classmethod
    def get_u_counter(cls):
        return f"User.user_counter = {cls.user_counter}."
    @classmethod
    def job(cls):
        return cls.user_counter ** 2 / 2
    @classmethod
    def ch_u_counter(cls, new_value):
        cls.user_counter = new_value

        
User.get_u_counter()
'User.user_counter = 0.'
User.ch_u_counter(777)
User.get_u_counter()
'User.user_counter = 777.'
u1 = User("Vasia", 77)
User.get_u_counter()
'User.user_counter = 778.'
User.__dict__
mappingproxy({'__module__': '__main__', '__firstlineno__': 1, 'user_counter': 778, '__init__': <function User.__init__ at 0x000001FBDD9E2020>, '__repr__': <function User.__repr__ at 0x000001FBDD9E20C0>, 'get_u_counter': <classmethod(<function User.get_u_counter at 0x000001FBDD9E2160>)>, 'job': <classmethod(<function User.job at 0x000001FBDD9E2200>)>, 'ch_u_counter': <classmethod(<function User.ch_u_counter at 0x000001FBDD9E22A0>)>, '__static_attributes__': ('age', 'name'), '__dict__': <attribute '__dict__' of 'User' objects>, '__weakref__': <attribute '__weakref__' of 'User' objects>, '__doc__': None})
help(User)
Help on class User in module __main__:

class User(builtins.object)
 |  User(n, a)
 |
 |  Methods defined here:
 |
 |  __init__(self, n, a)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  __repr__(self)
 |      Return repr(self).
 |
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |
 |  ch_u_counter(new_value)
 |
 |  get_u_counter()
 |
 |  job()
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
 |  user_counter = 778

class User:
    user_counter = 0
    def __init__(self, n, a):
        self.name = User.name_checker(n)
        self.age = a
        User.user_counter += 1
    def __repr__(self):
        return f"User({self.name}, {self.age})"
    @classmethod
    def get_u_counter(cls):
        return f"User.user_counter = {cls.user_counter}."
    @classmethod
    def job(cls):
        return cls.user_counter ** 2 / 2
    @classmethod
    def ch_u_counter(cls, new_value):
        cls.user_counter = new_value
    @staticmethod
    def name_checker(user_name):
        if len(user_name) < 3:
            return user_name * 4
        return user_name

    
u1 = User("Ag", 5)
u1
User(AgAgAgAg, 5)
u2 = User("Kate", 566)
u2
User(Kate, 566)
name = "Fa"
name = User.name_checker(name)
name
'FaFaFaFa'
u1 = User(name, 44)
u1
User(FaFaFaFa, 44)
u1 = User(User.name_checker(input("->")), 44)
->df
u1
User(dfdfdfdf, 44)
class User:
    user_counter = 0
    def __init__(self, n, a):
        self.name = User.name_checker(n)
        self.age = a
        User.user_counter += 1
    def __repr__(self):
        return f"User({self.name}, {self.age})"
    @classmethod
    def get_u_counter(cls):
        return f"User.user_counter = {cls.user_counter}."
    @classmethod
    def job(cls):
        return cls.user_counter ** 2 / 2
    @classmethod
    def ch_u_counter(cls, new_value):
        cls.user_counter = new_value
    @staticmethod
    def name_checker(user_name):
        if len(user_name) < 3:
            return user_name * 4
        return user_name
    @staticmethod
    def ret_true():
        return True

    
User.ret_true()
True




# Export
# python data --> txt, csv, xml
from abc import ABC, abstractmethod
class Export(ABC):
    @abstractmethod
    def preparation(self):
        pass
    @abstractmethod
    def export_prep_data(self):
        pass

    
class ExportTXT(Export):
    pass

class ExportTXT(Export):
    def __init__(self, data):
        self.data = data
    def preparation(self):
        pass
    def export_prep_data(self):
        pass

        

class ExportTXT(Export):
    def __init__(self, data):
        self.data = data
    def preparation(self):
        pass
    def export_prep_data(self):
        pass

    
from abc import ABC, abstractmethod
class Export(ABC):
    @abstractmethod
    def preparation(self):
        pass
    @abstractmethod
    def export_prep_data(self):
        pass

    
e = Export()
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    e = Export()
TypeError: Can't instantiate abstract class Export without an implementation for abstract methods 'export_prep_data', 'preparation'
class ExportTXT(Export):
    def __init__(self, data):
        self.data = data
    def preparation(self):
        pass

    
txt = ExportTXT("sdadada")
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    txt = ExportTXT("sdadada")
TypeError: Can't instantiate abstract class ExportTXT without an implementation for abstract method 'export_prep_data'
class ExportTXT(Export):
    def __init__(self, data):
        self.data = data
    def preparation(self):
        return data.upper()
    def export_prep_data(self):
        return "export txt" + self.preparation()

    
txt = ExportTXT("sdadada")
txt.export_prep_data()
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    txt.export_prep_data()
  File "<pyshell#115>", line 7, in export_prep_data
    return "export txt" + self.preparation()
  File "<pyshell#115>", line 5, in preparation
    return data.upper()
NameError: name 'data' is not defined. Did you mean: 'self.data'?
class ExportTXT(Export):
    def __init__(self, data):
        self.data = data
    def preparation(self):
        return self.data.upper()
    def export_prep_data(self):
        return "export txt" + self.preparation()

    
txt = ExportTXT("sdadada")
txt.export_prep_data()
'export txtSDADADA'
class ExportCSV(Export):
    def __init__(self, data):
        self.data = data
    def preparation(self):
        return self.data.upper()
    def export_prep_data(self):
        return "export csv" + self.preparation()

    
csv = ExportCSV("sdadada")
csv.export_prep_data()
'export csvSDADADA'
class ExportXML(Export):
    def __init__(self, data):
        self.data = data
    def export_prep_data(self):
        return "export xml" + self.preparation()

    
xml = ExportXML("sdadada")
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    xml = ExportXML("sdadada")
TypeError: Can't instantiate abstract class ExportXML without an implementation for abstract method 'preparation'




# 3 classes
# A(object)
# B(A)
# C(B)
# class var, inst var, method
class A:
    a = 1
    def __init__(self):
        self.aa = 11
    def fun_a(self):
        return "fun_a"

    
class B(A):
    b = 2
    def __init__(self):
        self.bb = 22
    def fun_b(self):
        return "fun_b"

    
class C(B):
    c = 3
    def __init__(self):
        self.cc = 33
    def fun_c(self):
        return "fun_c"

    
c_inst = C()
c_inst.cc
33
c_inst.c
3
c_inst.fun_c()
'fun_c'
c_inst.b
2
c_inst.bb
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    c_inst.bb
AttributeError: 'C' object has no attribute 'bb'
c_inst.fun_b()
'fun_b'
c_inst.a
1
c_inst.aa
Traceback (most recent call last):
  File "<pyshell#157>", line 1, in <module>
    c_inst.aa
AttributeError: 'C' object has no attribute 'aa'
c_inst.fun_a
<bound method A.fun_a of <__main__.C object at 0x000001FBDD8C6A50>>
c_inst.fun_a()
'fun_a'
class A:
    a = 1
    def __init__(self):
        self.aa = 11
    def fun_a(self):
        return "fun_a"

    
class B(A):
    b = 2
    def __init__(self):
        super().__init__()
        self.bb = 22
    def fun_b(self):
        return "fun_b"

    
class C(B):
    c = 3
    def __init__(self):
        super().__init__()
        self.cc = 33
    def fun_c(self):
        return "fun_c"

    
c_inst = C()
c_inst.c
3
c_inst.cc
33
c_inst.bb
22
c_inst.aa
11
C.mro()
[<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
B.mro()
[<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
A.mro()
[<class '__main__.A'>, <class 'object'>]



# A B --> C(a, b)
class A:
    a = 1
    variable = 100
    def __init__(self):
        self.aa = 11
    def fun_a(self):
        return "fun_a"

    
class B:
    b = 1
    variable = 333
    def __init__(self):
        self.bb = 11
    def fun_b(self):
        return "fun_b"

    
class C(A, B):
    pass

c_inst = C()
c_inst.a
1
c_inst.b
1
c_inst.variable
100
C.mro()
[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]



class A:
    def start(self):
        print("A - start")
    def job(self):
        self.start()

        
class B:
    def start(self):
        print("B - start")

        
class B(A):
    def start(self):
        print("B - start")

        
B.mro()
[<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
a_inst = A()
b_inst = B()
a_inst.start()
A - start
a_inst.job()
A - start
b_inst.start()
B - start
b_inst.job()
B - start
class A:
    def __str__(self):
        print("A - str")

class B(A):
    def __str__(self):
        print("B - str")

        
bb = B()
print(bb)
B - str
Traceback (most recent call last):
  File "<pyshell#214>", line 1, in <module>
    print(bb)
TypeError: __str__ returned non-string (type NoneType)
class A:
    def __str__(self):
        return "A - str"

    
class B(A):
    def __str__(self):
        return "B - str"

    
bb = B()

print(bb)
B - str



try:
    1 / 0
except:  # если была ошибка
    print(0)
else:  # усли в try не было ошибок
    print("OK")
finally:  # в любом случае выстрелит
    print("BUM!")

    
0
BUM!
try:
    print()
except:  # если была ошибка
    print(0)
else:  # усли в try не было ошибок
    print("OK")
finally:  # в любом случае выстрелит
    print("BUM!")

    

OK
BUM!
try:
    print()
except:  # если была ошибка
    print(0)
else:  # усли в try не было ошибок
    print("OK")

    

OK
try:
    prit()
except:  # если была ошибка
    print(0)
else:  # усли в try не было ошибок
    print("OK")

    
0
try:
    prit()
else:  # усли в try не было ошибок
    print("OK")
    
SyntaxError: expected 'except' or 'finally' block
try:
    prit()
finally:  # усли в try не было ошибок
    print("OK")

    
OK
Traceback (most recent call last):
  File "<pyshell#241>", line 2, in <module>
    prit()
NameError: name 'prit' is not defined. Did you mean: 'print'?
try:
    prit()
except:  # если была ошибка
    print(0)
else:  # усли в try не было ошибок
    print("OK")

    
0



class User:
    def __init__(self, n, a):
        self.name = n
        self.age = a
    def __repr__(self):
        return f"User({self.name}, {self.age})"

    
def user_input():
    n, a = input("name "), int(input("age "))
    if len(n) < 2:
        pass  ## вызвать исключение ОшибкаДлинна имени
    if a < 0:
        pass  ## вызвать исключение Ошибкавозраст отриц
    return User(n, a)

def user_input():
    n, a = input("name "), int(input("age "))
    if len(n) < 2:
        raise ZeroDivisionError ## вызвать исключение ОшибкаДлинна имени
    if a < 0:
        raise ZeroDivisionError  ## вызвать исключение Ошибкавозраст отриц
    return User(n, a)

user_input()
name f
age 55
Traceback (most recent call last):
  File "<pyshell#259>", line 1, in <module>
    user_input()
  File "<pyshell#258>", line 4, in user_input
    raise ZeroDivisionError ## вызвать исключение ОшибкаДлинна имени
ZeroDivisionError
class UserNameError(Exception):
    def __init__(self, u_name, message = "имя пользователя меньше 2 символов запрещено!"):
        self.u_name = u_name
        self.message = message

        
raise UserNameError("A")
Traceback (most recent call last):
  File "<pyshell#265>", line 1, in <module>
    raise UserNameError("A")
UserNameError: A
class UserNameError(Exception):
    def __init__(self, u_name, message = "имя пользователя меньше 2 символов запрещено!"):
        self.u_name = u_name
        self.message = message
    def __repr__(self):
        return self.message + "-->" + self.message

    
raise UserNameError("A")
Traceback (most recent call last):
  File "<pyshell#270>", line 1, in <module>
    raise UserNameError("A")
UserNameError: A
class UserAgeError(Exception):
    def __init__(self, u_age, message = "возраст пользователя  не может быть меньше 0!"):
        self.u_age = u_age
        self.message = message
    def __repr__(self):
        return f"{self.u_age} --> {self.message}"

    
raise UserAgeError("-1")
Traceback (most recent call last):
  File "<pyshell#273>", line 1, in <module>
    raise UserAgeError("-1")
UserAgeError: -1
def user_input():
    n, a = input("name "), int(input("age "))
    if len(n) < 2:
        raise UserNameError(n)
    if a < 0:
        raise UserAgeError(a)
    return User(n, a)

user_input()
name asdsad
age 44
User(asdsad, 44)
user_input()
name f
age 454
Traceback (most recent call last):
  File "<pyshell#277>", line 1, in <module>
    user_input()
  File "<pyshell#275>", line 4, in user_input
    raise UserNameError(n)
UserNameError: f
user_input()
name sdsd
age -5
Traceback (most recent call last):
  File "<pyshell#278>", line 1, in <module>
    user_input()
  File "<pyshell#275>", line 6, in user_input
    raise UserAgeError(a)
UserAgeError: -5
try:
    user_input()
except UserNameError as err:
    print(err)
except UserAgeError as err:
    print(err)
except:
    print("ne verno")

    
name a
age 44
a
class UserAgeError(Exception):
    def __init__(self, u_age, message = "возраст пользователя  не может быть меньше 0!"):
        self.u_age = u_age
        self.message = message
    def __str__(self):
        return f"{self.u_age} --> {self.message}"

    
try:
    user_input()
except UserNameError as err:
    print(err)
except UserAgeError as err:
    print(err)
except:
    print("ne verno")

    
name sdfsdf
age -4
-4 --> возраст пользователя  не может быть меньше 0!
class UserNameError(Exception):
    def __init__(self, u_name, message = "имя пользователя меньше 2 символов запрещено!"):
        self.u_name = u_name
        self.message = message
    def __str__(self):
        return self.message + "-->" + self.message

    
try:
    user_input()
except UserNameError as err:
    print(err)
except UserAgeError as err:
    print(err)
except:
    print("ne verno")

    
name f
age 4
имя пользователя меньше 2 символов запрещено!-->имя пользователя меньше 2 символов запрещено!
class UserNameError(Exception):
    def __init__(self, u_name, message = "имя пользователя меньше 2 символов запрещено!"):
        self.u_name = u_name
        self.message = message
    def __str__(self):
        return self.u_name + "-->" + self.message

    
try:
    user_input()
except UserNameError as err:
    print(err)
except UserAgeError as err:
    print(err)
except:
    print("ne verno")

    
name f
age 3
f-->имя пользователя меньше 2 символов запрещено!
try:
    user_input()
except UserNameError as err:
    print(err)
except UserAgeError as err:
    print(err)
except:
    print("ne verno")

    
name asda
age -5
-5 --> возраст пользователя  не может быть меньше 0!






# Que - put get __que = []
# exception - QueEmptyError

class Que:
    def __init__(self):
        self.__que = []
        print("Очередь создана")
    def put(self, number):
        self.__que.append(number)
        print("значение успешно добавлено")
    def get(self):
        if len(self.__que) < 1:
            raise EmptyQueError
        del self.__que[0]
        print("значение успешно удалено")

        
class EmptyQueError(Exception):
    """Очередь пуста"""
    pass

q1 = Que()
Очередь создана
for i in range(5):
    q1.put(i)

    
значение успешно добавлено
значение успешно добавлено
значение успешно добавлено
значение успешно добавлено
значение успешно добавлено
q1.__dict__
{'_Que__que': [0, 1, 2, 3, 4]}
q1.get()
значение успешно удалено
q1.get()
значение успешно удалено
q1.get()
значение успешно удалено
q1.get()
значение успешно удалено
q1.get()
значение успешно удалено
q1.get()
Traceback (most recent call last):
  File "<pyshell#336>", line 1, in <module>
    q1.get()
  File "<pyshell#321>", line 10, in get
    raise EmptyQueError
EmptyQueError
for i in range(5):
    q1.put(i)

    
значение успешно добавлено
значение успешно добавлено
значение успешно добавлено
значение успешно добавлено
значение успешно добавлено
q1.__dict__
{'_Que__que': [0, 1, 2, 3, 4]}
q1.get()
значение успешно удалено
q1.__dict__
{'_Que__que': [1, 2, 3, 4]}
q1.get()
значение успешно удалено
q1.__dict__
{'_Que__que': [2, 3, 4]}
q1.get()
значение успешно удалено
q1.get()
значение успешно удалено
q1.get()
значение успешно удалено
q1.get()
Traceback (most recent call last):
  File "<pyshell#347>", line 1, in <module>
    q1.get()
  File "<pyshell#321>", line 10, in get
    raise EmptyQueError
EmptyQueError
q1.__dict__
{'_Que__que': []}
class Que:
    def __init__(self):
        self.__que = []
        print("Очередь создана")
    def put(self, number):
        self.__que.append(number)
        print("значение успешно добавлено")
        print("текущее знач.очереди:", self.__que)
        print()
    def get(self):
        if len(self.__que) < 1:
            raise EmptyQueError
        del self.__que[0]
        print("значение успешно удалено")
        print("текущее знач.очереди:", self.__que)
        print()

        
for i in range(5):
    q1.put(i)

    
значение успешно добавлено
значение успешно добавлено
значение успешно добавлено
значение успешно добавлено
значение успешно добавлено
q1 = Que()
Очередь создана
for i in range(5):
    q1.put(i)

    
значение успешно добавлено
текущее знач.очереди: [0]

значение успешно добавлено
текущее знач.очереди: [0, 1]

значение успешно добавлено
текущее знач.очереди: [0, 1, 2]

значение успешно добавлено
текущее знач.очереди: [0, 1, 2, 3]

значение успешно добавлено
текущее знач.очереди: [0, 1, 2, 3, 4]

>>> for i in range(6):
...     q1.get()
... 
...     
значение успешно удалено
текущее знач.очереди: [1, 2, 3, 4]

значение успешно удалено
текущее знач.очереди: [2, 3, 4]

значение успешно удалено
текущее знач.очереди: [3, 4]

значение успешно удалено
текущее знач.очереди: [4]

значение успешно удалено
текущее знач.очереди: []

Traceback (most recent call last):
  File "<pyshell#358>", line 2, in <module>
    q1.get()
  File "<pyshell#351>", line 12, in get
    raise EmptyQueError
EmptyQueError
