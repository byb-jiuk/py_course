Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class A:
    def __init__(self, f, b)):
        
SyntaxError: unmatched ')'
# Singleton
class Singleton:
    pass

s1 = Singleton()
s2 = Singleton()
class Singleton:
    __instance = None
    def __init__(self):
        if Singleton.__instance is None:
            Singleton.__instance = self
        else:
            raise Exception("У данного класса может юыть только один экз")

        
s1 = Singleton()
s2 = Singleton()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    s2 = Singleton()
  File "<pyshell#14>", line 7, in __init__
    raise Exception("У данного класса может юыть только один экз")
Exception: У данного класса может юыть только один экз
Singleton.__dict__
mappingproxy({'__module__': '__main__', '__firstlineno__': 1, '_Singleton__instance': <__main__.Singleton object at 0x0000025CAFB6ABA0>, '__init__': <function Singleton.__init__ at 0x0000025CAFC51800>, '__static_attributes__': (), '__dict__': <attribute '__dict__' of 'Singleton' objects>, '__weakref__': <attribute '__weakref__' of 'Singleton' objects>, '__doc__': None})


# Database
class DatabaseConnection:
    __instance = None
    def __init__(self, database_name):
        if DatabaseConnection.__instance is None:
            DatabaseConnection.__instance = self
            self.database_name = database_name
        else:
            raise Exception("У данного класса может юыть только один экз")
    def __rep__(self):
        retyrn f"Соединние с БД {self.database_name}"
        
SyntaxError: invalid syntax

class DatabaseConnection:
    __instance = None
    def __init__(self, database_name):
        if DatabaseConnection.__instance is None:
            DatabaseConnection.__instance = self
            self.database_name = database_name
        else:
            raise Exception("У данного класса может юыть только один экз")
    def __rep__(self):
        return f"Соединние с БД {self.database_name}"

    
DatabaseConnection._DatabaseConnection__instance
print(DatabaseConnection._DatabaseConnection__instance)
None


class MultipleDatabaseConnectionError(Exception):
    pass

class DatabaseConnection:
    __instance = None
    def __init__(self, database_name):
        if DatabaseConnection.__instance is None:
            DatabaseConnection.__instance = self
            self.database_name = database_name
        else:
            raise MultipleDatabaseConnectionError
    def __rep__(self):
        return f"Соединние с БД {self.database_name}"

    
conn = DatabaseConnection("account_info.db")
conn
<__main__.DatabaseConnection object at 0x0000025CAFB6AA50>
class DatabaseConnection:
    __instance = None
    def __init__(self, database_name):
        if DatabaseConnection.__instance is None:
            DatabaseConnection.__instance = self
            self.database_name = database_name
        else:
            raise MultipleDatabaseConnectionError
    def __repr__(self):
        return f"Соединние с БД {self.database_name}"

    
conn = DatabaseConnection("account_info.db")
conn
Соединние с БД account_info.db
conn1 = DatabaseConnection("accousnt_info.db")
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    conn1 = DatabaseConnection("accousnt_info.db")
  File "<pyshell#39>", line 8, in __init__
    raise MultipleDatabaseConnectionError
MultipleDatabaseConnectionError








# Creator Sub
# Creator - [Sub1, Sub2]
# Creator - createpost
#Creator - notifyall
# Creator - subscribe()


class Creator:
    def __init__(self):
        self.sub_list = []
        self.creator_name = name
    def follow(self, follower):
        sub_list.append(follower)
    def show_followers(self):
        print(self.sub_list)

        
creator1 = Creator("MyChannel")
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    creator1 = Creator("MyChannel")
TypeError: Creator.__init__() takes 1 positional argument but 2 were given
class Creator:
    def __init__(self, name):
        self.sub_list = []
        self.creator_name = name
    def follow(self, follower):
        self.sub_list.append(follower)
    def show_followers(self):
        print(self.sub_list)

        
creator1 = Creator("MyChannel")
creator1.show_followers
<bound method Creator.show_followers of <__main__.Creator object at 0x0000025CAFB6AE40>>
creator1.follow("Petya")
creator1.follow("Kate")
creator1.follow("Vald")
class Creator:
    def __init__(self, name):
        self.sub_list = []
        self.creator_name = name
    def follow(self, follower):
        self.sub_list.append(follower)
    def show_followers(self):
        print(self.sub_list)
    def create_post(self, message):
        print(self.creator_name, "publish message:")
        print(message)
        print()

        
creator1 = Creator("MyChannel")
creator1.create_post("i go dinner")
MyChannel publish message:
i go dinner

class Follower:
    def __init__(self, name):
        self.follower_name = name
    def react(self):
        print(self.follower_name, "Like a message")
    def __str__(self):
        return f"follower({self.follower_name})"
    def __repr__(self):
        return f"rep follower({self.follower_name})"

    
class Creator:
    def __init__(self, name):
        self.sub_list = []
        self.creator_name = name
    def follow(self, follower):
        self.sub_list.append(follower)
    def show_followers(self):
        print(self.sub_list)
    def notify_all(self):
        for follower in self.sub_list:
            follower.react()
    def create_post(self, message):
        print(self.creator_name, "publish message:")
        print(message)
        print()
        self.notify_all()

        
creator1 = Creator("MyChannel")
f1 = Follower("Petya")
f2 = Follower("Dimas")
f3 = Follower("Koly")
creator1.show_followers()
[]
creator1.create_post("run")
MyChannel publish message:
run

creator1.follow(f1)
creator1.show_followers()
[rep follower(Petya)]
creator1.create_post("run")
MyChannel publish message:
run

Petya Like a message
creator1.follow(f3)
creator1.show_followers()
[rep follower(Petya), rep follower(Koly)]
creator1.create_post("run")
MyChannel publish message:
run

Petya Like a message
Koly Like a message
creator1.create_post("I go walk")
MyChannel publish message:
I go walk

Petya Like a message
Koly Like a message
creator1.follow(f2)
creator1.show_followers()
[rep follower(Petya), rep follower(Koly), rep follower(Dimas)]
creator1.create_post("I go walk")
MyChannel publish message:
I go walk

Petya Like a message
Koly Like a message
Dimas Like a message













# Decorator



def add_five(number)
SyntaxError: expected ':'
def add_five(number):
    return number + 5

add_five(4)
9



def change(func):
    def inner(inner_number):
        func(inner_number*2)
    return inner

@change
def add_five(number):
    return number + 5

add_five(5)
def change(func):
    def inner(inner_number):
        return func(inner_number*2)
    return inner

@change
def add_five(number):
    return number + 5

add_five(5)
15


def change(func):
    print("Decor eat name func")
    def inner(inner_number):
        print("вместо оригинала запущенна иннер функция")
        return func(inner_number*2)
    return inner

@change
def add_five(number):
    print("и только тут я вызвал оригинальную функцию add_five")
    return number + 5

Decor eat name func
add_five
<function change.<locals>.inner at 0x0000025CAFC52F20>
add_five(3)
вместо оригинала запущенна иннер функция
и только тут я вызвал оригинальную функцию add_five
11


def change(func):
    print("Decor eat name func")
    def inner(inner_number):
        print("вместо оригинала запущенна иннер функция")
        return func(inner_number*2)
    return inner





def sub_five(number):
    print("и только тут я вызвал оригинальную функцию add_five")
    return number - 5

sub_five(5)
и только тут я вызвал оригинальную функцию add_five
0
@change
def sub_five(number):
    print("и только тут я вызвал оригинальную функцию add_five")
    return number - 5

Decor eat name func
sub_five(5)
вместо оригинала запущенна иннер функция
и только тут я вызвал оригинальную функцию add_five
5






# file + try + exce + fin


import os
os.getcwd()
'C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python313'
help(open)



fstream = open("my_first_txt_file.txt", "w")
try:
    fstream.write("1 Привет мир!\n")
    fstream.write("2 Привет мир!\n")
    fstream.write("3 Привет мир!\n")
    fstream.write("4 Привет мир!\n")
    fstream.write("5 Привет мир!\n")
    fstream.write("6 Привет мир!\n")
except:
    print("up")
finally:
    fstream.close()

    
14
14
14
14
14
14
fstream.write("1 Привет мир!\n")
Traceback (most recent call last):
  File "<pyshell#193>", line 1, in <module>
    fstream.write("1 Привет мир!\n")
ValueError: I/O operation on closed file.



os.getcwd()
'C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python313'



help("with")

>>> 
>>> 
>>> 
>>> with open("my_second_txt_file.txt", "w") as fs:
...     fstream.write("1 Привет мир!\n")
...     fstream.write("2 Привет мир!\n")
...     fstream.write("3 Привет мир!\n")
...     fstream.write("4 Привет мир!\n")
...     fstream.write("5 Привет мир!\n")
...     fstream.write("6 Привет мир!\n")
... 
...     
Traceback (most recent call last):
  File "<pyshell#207>", line 2, in <module>
    fstream.write("1 Привет мир!\n")
ValueError: I/O operation on closed file.
>>> with open("my_second_txt_file.txt", "w") as fstream:
...     fstream.write("1 Привет мир!\n")
...     fstream.write("2 Привет мир!\n")
...     fstream.write("3 Привет мир!\n")
...     fstream.write("4 Привет мир!\n")
...     fstream.write("5 Привет мир!\n")
...     fstream.write("6 Привет мир!\n")
... 
...     
14
14
14
14
14
14
>>> fstream
<_io.TextIOWrapper name='my_second_txt_file.txt' mode='w' encoding='cp1251'>
>>> fstream.write("1 Привет мир!\n")
Traceback (most recent call last):
  File "<pyshell#211>", line 1, in <module>
    fstream.write("1 Привет мир!\n")
ValueError: I/O operation on closed file.
