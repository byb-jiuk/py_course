Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
1 + 1
2
print("asdfasd")
asdfasd
li = [1,2,3,4,5,6]

li
[1, 2, 3, 4, 5, 6]
li[-1]
6


n= int(input("-->"))
-->12
1/n
0.08333333333333333
n= int(input("-->"))
-->0
1/n
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    1/n
ZeroDivisionError: division by zero
n= int(input("-->"))
-->sdfsdf
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    n= int(input("-->"))
ValueError: invalid literal for int() with base 10: 'sdfsdf'



n = input("-->")
-->123
n.isdigit()
True
if n.isdigit():
    print(1/int(n))

    
0.008130081300813009



# try except
except
SyntaxError: invalid syntax
except:
    
SyntaxError: invalid syntax
try
SyntaxError: expected ':'
try:
    n= int(input("-->"))
    print(1/n)
except:
    print("Хьюстон у нас проблемы...(^_^)")

    
-->sdfasda
Хьюстон у нас проблемы...(^_^)
try:
    n= int(input("-->"))
    print(1/n)
except:
    print("Хьюстон у нас проблемы...(^_^)")

    
-->0
Хьюстон у нас проблемы...(^_^)
try:
    n= int(input("-->"))
    print(1/n)
except:
    print("Хьюстон у нас проблемы...(^_^)")

    
-->123
0.008130081300813009


for i in range(4):
    try:
        n= int(input("-->"))
        print(1/n)
    except:
        print("Хьюстон у нас проблемы...(^_^)")

        
-->5
0.2
-->0
Хьюстон у нас проблемы...(^_^)
-->adsd
Хьюстон у нас проблемы...(^_^)
-->-1
-1.0
for i in range(4):
        n= int(input("-->"))
        print(1/n)

        
-->2
0.5
-->0
Traceback (most recent call last):
  File "<pyshell#56>", line 3, in <module>
    print(1/n)
ZeroDivisionError: division by zero


#ValueError, ZeroDivisionError

try:
    n= int(input("-->"))
    print(1/n)
except:
    print("Хьюстон у нас проблемы...(^_^)")

    
-->ff
Хьюстон у нас проблемы...(^_^)
try:
    n= int(input("-->"))
    print(1/n)
except ValueError:
    print("Value error - sorry...")
except:
    print("Хьюстон у нас проблемы...(^_^)")

    
-->123
0.008130081300813009
try:
    n= int(input("-->"))
    print(1/n)
except ValueError:
    print("Value error - sorry...")
except:
    print("Хьюстон у нас проблемы...(^_^)")

    
-->0
Хьюстон у нас проблемы...(^_^)
try:
    n= int(input("-->"))
    print(1/n)
except ValueError:
    print("Value error - sorry...")
except:
    print("Хьюстон у нас проблемы...(^_^)")

    
-->asd
Value error - sorry...
try:
    n= int(input("-->"))
    print(1/n)
except ValueError:
    print("Value error - sorry...")

    
-->123
0.008130081300813009
try:
    n= int(input("-->"))
    print(1/n)
except ValueError:
    print("Value error - sorry...")

    
-->sdfdsf
Value error - sorry...
try:
    n= int(input("-->"))
    print(1/n)
except ValueError:
    print("Value error - sorry...")

    
-->0
Traceback (most recent call last):
  File "<pyshell#74>", line 3, in <module>
    print(1/n)
ZeroDivisionError: division by zero


try:
    n= int(input("-->"))
    print(1/n)
except ValueError:
    print("Value error - sorry...")
except ZeroDivisionError:
    print("Delit na 0 nizy")

    
-->0
Delit na 0 nizy
try:
    n= int(input("-->"))
    print(1/n)
except ValueError:
    print("Value error - sorry...")
except ZeroDivisionError:
    print("Delit na 0 nizy")
except:
    print("Хьюстон у нас проблемы...(^_^)")

    
-->12
0.08333333333333333
try:
    n= int(input("-->"))
    print(1/n)
except ValueError:
    print("Value error - sorry...")
except ZeroDivisionError:
    print("Delit na 0 nizy")
except:
    print("Хьюстон у нас проблемы...(^_^)")

    
-->sdf
Value error - sorry...
try:
    n= int(input("-->"))
    print(1/n)
except ValueError:
    print("Value error - sorry...")
except ZeroDivisionError:
    print("Delit na 0 nizy")
except:
    print("Хьюстон у нас проблемы...(^_^)")

    
-->0
Delit na 0 nizy
try:
    n= int(input("-->"))
    print(1/n)
except ValueError:
    print("Value error - sorry...")
except ZeroDivisionError:
    print("Delit na 0 nizy")
try:
    n= int(input("-->"))
    print(1/n)
except ValueError:
    print("Value error - sorry...")
try:
    n= int(input("-->"))
    print(1/n)
except ValueError:
    print("Value error - sorry...")
except ZeroDivisionError:
    print("Delit na 0 nizy")
except:
    print("Хьюстон у нас проблемы...(^_^)")
except ZeroDivisionError:
    print("Delit na 0 nizy")
    
SyntaxError: invalid syntax

try:
    n= int(input("-->"))
    print(1/n)
except ValueError:
    print("Value error - sorry...")
except ZeroDivisionError:
    print("Delit na 0 nizy")
except:
    print("Хьюстон у нас проблемы...(^_^)")
except ZeroDivisionError:
    print("Delit na 0 nizy")
    
SyntaxError: default 'except:' must be last
+
SyntaxError: invalid syntax

a = 1
if a == 1:
    print(10)
else:
    print(33)
elif a == 55:
    print(22)
    
SyntaxError: invalid syntax


try:
    n= int(input("-->"))
    print(1/n)
except Exception as e:
    print(e)
    print(e.args)
    print(e.__traceback__)

    
-->sada
invalid literal for int() with base 10: 'sada'
("invalid literal for int() with base 10: 'sada'",)
<traceback object at 0x000002082C299880>
try:
    n= int(input("-->"))
    print(1/n)
except Exception as e:
    print(type(e))
    print(e.args)
    print(e.__traceback__)

    
-->sdfsf
<class 'ValueError'>
("invalid literal for int() with base 10: 'sdfsf'",)
<traceback object at 0x000002082EC69EC0>
try:
    n= int(input("-->"))
    print(1/n)
except Exception as e:
    print(type(e))
    print(e.args)
    print(e.__traceback__)

    
-->656
0.001524390243902439
try:
    n= int(input("-->"))
    print(1/n)
except ValueError as ve:
    print("Value error - sorry...")
    print(type(ve))
    print(ve.args)
except ZeroDivisionError as zde:
    print("Delit na 0 nizy")
    print(type(zde))
    print(zde.args[0])   
except:
    print("Хьюстон у нас проблемы...(^_^)")

    
-->454
0.0022026431718061676
try:
    n= int(input("-->"))
    print(1/n)
except ValueError as ve:
    print("Value error - sorry...")
    print(type(ve))
    print(ve.args)
except ZeroDivisionError as zde:
    print("Delit na 0 nizy")
    print(type(zde))
    print(zde.args[0])   
except:
    print("Хьюстон у нас проблемы...(^_^)")

    
-->sdfsdf
Value error - sorry...
<class 'ValueError'>
("invalid literal for int() with base 10: 'sdfsdf'",)
try:
    n= int(input("-->"))
    print(1/n)
except ValueError as ve:
    print("Value error - sorry...")
    print(type(ve))
    print(ve.args)
except ZeroDivisionError as zde:
    print("Delit na 0 nizy")
    print(type(zde))
    print(zde.args[0])   
except:
    print("Хьюстон у нас проблемы...(^_^)")

    
-->0
Delit na 0 nizy
<class 'ZeroDivisionError'>
division by zero


import traceback
try:
    n= int(input("-->"))
    print(1/n)
except ValueError as ve:
    print("Value error - sorry...")
    print(type(ve))
    print(ve.args)
    traceback.print_tb(ve.__traceback__)
except ZeroDivisionError as zde:
    print("Delit na 0 nizy")
    print(type(zde))
    print(zde.args[0])
    traceback.print_tb(zde.__traceback__)
except:
    print("Хьюстон у нас проблемы...(^_^)")

    
-->sdfsdf
Value error - sorry...
<class 'ValueError'>
("invalid literal for int() with base 10: 'sdfsdf'",)
  File "<pyshell#117>", line 2, in <module>
try:
    n= int(input("-->"))
    print(1/n)
except ValueError as ve:
    print("Value error - sorry...")
    print(type(ve))
    print(ve.args)
    traceback.print_tb(ve.__traceback__)
except ZeroDivisionError as zde:
    print("Delit na 0 nizy")
    print(type(zde))
    print(zde.args[0])
    traceback.print_tb(zde.__traceback__)
except:
    print("Хьюстон у нас проблемы...(^_^)")

    
-->0
Delit na 0 nizy
<class 'ZeroDivisionError'>
division by zero
  File "<pyshell#119>", line 3, in <module>
try:
    n= int(input("-->"))
    print(1/n)
except ValueError as ve:
    print("Value error - sorry...")
    print(type(ve))
    print(ve.args)
    traceback.print_exc(ve)
except ZeroDivisionError as zde:
    print("Delit na 0 nizy")
    print(type(zde))
    print(zde.args[0])
    traceback.print_exc(zde)
except:
    print("Хьюстон у нас проблемы...(^_^)")

    
-->0
Delit na 0 nizy
<class 'ZeroDivisionError'>
division by zero
Traceback (most recent call last):
  File "<pyshell#121>", line 3, in <module>
    print(1/n)
ZeroDivisionError: division by zero

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#121>", line 13, in <module>
    traceback.print_exc(zde)
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python313\Lib\traceback.py", line 208, in print_exc
    print_exception(sys.exception(), limit=limit, file=file, chain=chain)
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python313\Lib\traceback.py", line 129, in print_exception
    te = TracebackException(type(value), value, tb, limit=limit, compact=True)
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python313\Lib\traceback.py", line 1044, in __init__
    self.stack = StackSummary._extract_from_extended_frame_gen(
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python313\Lib\traceback.py", line 465, in _extract_from_extended_frame_gen
    elif limit >= 0:
TypeError: '>=' not supported between instances of 'ZeroDivisionError' and 'int'
try:
    n= int(input("-->"))
    print(1/n)
except ValueError as ve:
    print("Value error - sorry...")
    print(type(ve))
    print(ve.args)
    traceback.print_exc(ve)
except ZeroDivisionError as zde:
    print("Delit na 0 nizy")
    print(type(zde))
    print(zde.args[0])
    traceback.print_exc(zde)
except:
    print("Хьюстон у нас проблемы...(^_^)")

    
-->5
0.2












n= input("-->")
-->1
if n == 1:
    print(1)
elif n == 2:
    asdasdasd()
elif n == 3:
    prin(3)
else:
    print(123)

    
123
n= int(input("-->"))
-->1
if n == 1:
    print(1)
elif n == 2:
    asdasdasd()
elif n == 3:
    prin(3)
else:
    print(123)

    
1
n= int(input("-->"))
-->55
if n == 1:
    print(1)
elif n == 2:
    asdasdasd()
elif n == 3:
    prin(3)
else:
    print(123)

    
123
n= int(input("-->"))
-->3
if n == 1:
    print(1)
elif n == 2:
    asdasdasd()
elif n == 3:
    prin(3)
else:
    print(123)

    
Traceback (most recent call last):
  File "<pyshell#154>", line 6, in <module>
    prin(3)
NameError: name 'prin' is not defined. Did you mean: 'print'?
n= int(input("-->"))
-->2
if n == 1:
    print(1)
elif n == 2:
    asdasdasd()
elif n == 3:
    prin(3)
else:
    print(123)

    
Traceback (most recent call last):
  File "<pyshell#157>", line 4, in <module>
    asdasdasd()
NameError: name 'asdasdasd' is not defined



# BaseException -> Exception
# Exception --> ArithmeticError ---> ZeroDiverr


try:
    1/0
except ZeroDivisionError:
    print("ZeroDivisionError")

    
ZeroDivisionError
try:
    1/0
except ArithmeticError:
    print("ArithmeticError")

    
ArithmeticError
try:
    1/0
except Exception:
    print("Exception")

    
Exception
try:
    1/0
except Exception:
    print("Exception")
except ArithmeticError:
    print("ArithmeticError")
except ZeroDivisionError:
    print("ZeroDivisionError")

    
Exception
try:
    1/0
except ZeroDivisionError:
    print("ZeroDivisionError")
except ArithmeticError:
    print("ArithmeticError")
except Exception:
    print("Exception")

    
ZeroDivisionError
try:
    1/0
except ZeroDivisionError:
    print("ZeroDivisionError")
except ArithmeticError:
    print("ArithmeticError")
except Exception:
    print("Exception")

    
ZeroDivisionError

# BaseException -> Exception
# Exception --> LookupError
# LookupError --> IndexError
#LookupError --> KeyError

try:
    1/0
except ZeroDivisionError:
    print("ZeroDivisionError")
except ArithmeticError:
    print("ArithmeticError")
except Exception:
    print("Exception")
except IndexError:
    print("IndexError")

    
ZeroDivisionError
li = [1,2,3]
try:
    li[123123]
except ZeroDivisionError:
    print("ZeroDivisionError")
except ArithmeticError:
    print("ArithmeticError")
except Exception:
    print("Exception")
except IndexError:
    print("IndexError")

    
Exception
try:
    li[123123]
except IndexError:
    print("IndexError")
except ZeroDivisionError:
    print("ZeroDivisionError")
except ArithmeticError:
    print("ArithmeticError")
except:
    print("default")

    
IndexError
try:
    1/0
except IndexError:
    print("IndexError")
except ZeroDivisionError:
    print("ZeroDivisionError")
except ArithmeticError:
    print("ArithmeticError")
except:
    print("default")

    
ZeroDivisionError


dir
<built-in function dir>
help(dir)
Help on built-in function dir in module builtins:

dir(...)
    dir([object]) -> list of strings

    If called without an argument, return the names in the current scope.
    Else, return an alphabetized list of names comprising (some of) the attributes
    of the given object, and of attributes reachable from it.
    If the object supplies a method named __dir__, it will be used; otherwise
    the default dir() logic is used and returns:
      for a module object: the module's attributes.
      for a class object:  its attributes, and recursively the attributes
        of its bases.
      for any other object: its attributes, its class's attributes, and
        recursively the attributes of its class's base classes.

dir(Exception)
['__cause__', '__class__', '__context__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__suppress_context__', '__traceback__', 'add_note', 'args', 'with_traceback']



n = 10
x  = int(input("-->"))
-->1
try:
    n/x
except ZeroDivisionError:
    print("Ne deli na 0...")

    
10.0
try:
    raise ZeroDivisionError
except ZeroDivisionError:
    print("Ne deli na 0...")

    
Ne deli na 0...
try:
    n/x
except ZeroDivisionError:
    print("Ne deli na 0...")

    
10.0



def a():
    raise ZeroDivisionError

a()
Traceback (most recent call last):
  File "<pyshell#224>", line 1, in <module>
    a()
  File "<pyshell#223>", line 2, in a
    raise ZeroDivisionError
ZeroDivisionError
def a():
    try:
        raise ZeroDivisionError
    except:
        print("ok inside")

        
a()
ok inside
def a():
    try:
        raise ZeroDivisionError
    except:
        print("ok inside")
        raise

    
a()
ok inside
Traceback (most recent call last):
  File "<pyshell#233>", line 1, in <module>
    a()
  File "<pyshell#232>", line 3, in a
    raise ZeroDivisionError
ZeroDivisionError
try:
    a()
except:
    print("ok outside")

    
ok inside
ok outside


assert 0
Traceback (most recent call last):
  File "<pyshell#241>", line 1, in <module>
    assert 0
AssertionError
assert False
Traceback (most recent call last):
  File "<pyshell#242>", line 1, in <module>
    assert False
AssertionError
>>> assert []
Traceback (most recent call last):
  File "<pyshell#243>", line 1, in <module>
    assert []
AssertionError
>>> assert ()
Traceback (most recent call last):
  File "<pyshell#244>", line 1, in <module>
    assert ()
AssertionError
>>> assert {}
Traceback (most recent call last):
  File "<pyshell#245>", line 1, in <module>
    assert {}
AssertionError
>>> assert None
Traceback (most recent call last):
  File "<pyshell#246>", line 1, in <module>
    assert None
AssertionError
>>> assert 1
>>> assert True
>>> assert [1,]
>>> 
>>> 
>>> def a(n):
...     return True if n % 2 == 0 else False
... 
>>> res = [(2, True), (3, False), (4, True)]
>>> assert a(res[0][0]) == res[0][1]
>>> assert a(res[1][0]) == res[1][1]
>>> res = [(2, True), (3, False), (4, True), (5, True)]
>>> assert a(res[3][0]) == res[3][1]
Traceback (most recent call last):
  File "<pyshell#259>", line 1, in <module>
    assert a(res[3][0]) == res[3][1]
AssertionError
>>> [DEBUG ON]
>>> [DEBUG OFF]
