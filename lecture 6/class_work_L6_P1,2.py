Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

print(123)
123
1+5
6
li=[1,2,3,4]
len(li)
4
li[1]
2





finelds = ("name", "phone", 123123, 123 , 234)
type(fields)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    type(fields)
NameError: name 'fields' is not defined. Did you mean: 'finelds'?
fields = ("name", "phone", 123123, 123 , 234)
type(fields)
<class 'tuple'>
print(fields)
('name', 'phone', 123123, 123, 234)




#empty tuples

to = ()
type(tp)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    type(tp)
NameError: name 'tp' is not defined
tp1 = tuple()
type(tp1)
<class 'tuple'>
tp1
()
isinstance(tp, tuple)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    isinstance(tp, tuple)
NameError: name 'tp' is not defined
isinstance(to, tuple)
True

li = [1]
li
[1]
se = {1}
se
{1}

# one element tuple
tp = (1)
type(tp)
<class 'int'>
tp = 1
tp
1
tp = (1,)
type(tp)
<class 'tuple'>
tp
(1,)
tp = 1,
tp
(1,)
li = [1,2,3]
se = {1,2,3}
st = "12312"
i = 1
f = 5.4
tp = (1,2,3)
tp
(1, 2, 3)
li
[1, 2, 3]
se
{1, 2, 3}
st
'12312'
i
1
f
5.4
tp = 1, 2, 3
tp = (1,2,3)
tp[0]
1
tp[1]
2
tp[3]
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    tp[3]
IndexError: tuple index out of range
tp[3]
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    tp[3]
IndexError: tuple index out of range
li
[1, 2, 3]
se
{1, 2, 3}
st
'12312'
tp
(1, 2, 3)
len(li)
3
len(st)
5
len(se)
3
len(tp)
3


tp
(1, 2, 3)
tp[-1]
3
tp
(1, 2, 3)
tp[::-1]
(3, 2, 1)


tp = (1., 2., 3., .4,)
tp
(1.0, 2.0, 3.0, 0.4)
# unchangeable

li
[1, 2, 3]
li.append(123)
li
[1, 2, 3, 123]
li[0] = 999
li
[999, 2, 3, 123]
tp.append(213)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    tp.append(213)
AttributeError: 'tuple' object has no attribute 'append'
tp[0] = 444
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    tp[0] = 444
TypeError: 'tuple' object does not support item assignment
li
[999, 2, 3, 123]
tp
(1.0, 2.0, 3.0, 0.4)
tp = (1.0, 2.0, 3.0, 0.4, li)
tp
(1.0, 2.0, 3.0, 0.4, [999, 2, 3, 123])
li.pop()
123
tp
(1.0, 2.0, 3.0, 0.4, [999, 2, 3])


# unpack


li = [1,2,3,45]
tp = (1,2,3,45)

a,b,c,d = tp
a
1
d
45
st = "12345"
a,b,c,d,e = st
e
'5'
c
'3'
tp = (1,2,3)
number, *fields = tp
number
1
fields
[2, 3]


def ret_tuple():
    return (1,2,3,4,5)

ret_tuple()
(1, 2, 3, 4, 5)
res = ret_tuple()
res
(1, 2, 3, 4, 5)
g, *h = ret_tuple()
g
1
h
[2, 3, 4, 5]
h.append(123213)
h
[2, 3, 4, 5, 123213]
# str list tuple set
def ret_tuple():
    return (1,2,3,4,5)

a, *b, c = ret_tuple()
b
[2, 3, 4]
a
1
c
5
a, *b, c, d = ret_tuple()
b
[2, 3]
c
4
d
5
a
1
a, *b, c, d, e = ret_tuple()
b
[2]
ret_tuple()
(1, 2, 3, 4, 5)
*a = ret_tuple()
SyntaxError: starred assignment target must be in a list or tuple
ret_tuple()
(1, 2, 3, 4, 5)
*a, b = ret_tuple()
a
[1, 2, 3, 4]
b
5



tp = 1,
tp
(1,)
tp = 3.,
tp
(3.0,)



tp = 1,2,3,4,5,6
tp
(1, 2, 3, 4, 5, 6)
tp[:3]
(1, 2, 3)
tp[3:]
(4, 5, 6)
tp[::2]
(1, 3, 5)
tp[::-1]
(6, 5, 4, 3, 2, 1)
tp2 = 2,3,4,5,6
tp2
(2, 3, 4, 5, 6)
tp + tp2
(1, 2, 3, 4, 5, 6, 2, 3, 4, 5, 6)
tp * 5
(1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6)
tp  * 3
(1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6)
3 * tp2
(2, 3, 4, 5, 6, 2, 3, 4, 5, 6, 2, 3, 4, 5, 6)

tp
(1, 2, 3, 4, 5, 6)
6 in tp
True
77 im tp
SyntaxError: invalid syntax
77 in tp
False
123123123in tp
False
2in tp
True
2 in tp
True
tp
(1, 2, 3, 4, 5, 6)
2in tp
True
tp
(1, 2, 3, 4, 5, 6)
tp2
(2, 3, 4, 5, 6)
tp, tp2 = tp2, tp
tp
(2, 3, 4, 5, 6)
tp2
(1, 2, 3, 4, 5, 6)



tp
(2, 3, 4, 5, 6)
tp[:3]
(2, 3, 4)
tp[-1]
6
(22,33,44)
(22, 33, 44)
1 + (12,3,)
Traceback (most recent call last):
  File "<pyshell#192>", line 1, in <module>
    1 + (12,3,)
TypeError: unsupported operand type(s) for +: 'int' and 'tuple'
result_tuple = tp[:3] + (22, 33, 44) + tp[4:]
tp[4:]
(6,)
result_tuple
(2, 3, 4, 22, 33, 44, 6)


del result_tuple
result_tuple
Traceback (most recent call last):
  File "<pyshell#199>", line 1, in <module>
    result_tuple
NameError: name 'result_tuple' is not defined. Did you mean: 'ret_tuple'?
tp
(2, 3, 4, 5, 6)
tp.count(3)
1
tp.count(33)
0
tp.index(4)
2



n = int(input())
5
n
5
tp
(2, 3, 4, 5, 6)
if n in tp:
    print("index:", tp.index(n))
    print("value:", tp[tp.index(n)])

    
index: 3
value: 5
n = 99
tp.index(n)
Traceback (most recent call last):
  File "<pyshell#215>", line 1, in <module>
    tp.index(n)
ValueError: tuple.index(x): x not in tuple



tp
(2, 3, 4, 5, 6)
tp = tp[:3]
tp
(2, 3, 4)
tp = (2, 3, 4, 5, 6)
tp = tuple(list(tp).pop().pop())
Traceback (most recent call last):
  File "<pyshell#223>", line 1, in <module>
    tp = tuple(list(tp).pop().pop())
AttributeError: 'int' object has no attribute 'pop'
tp = tuple(list(tp))
tp = list(tp)
tp.pop()
6
tp.pop()
5
tp
[2, 3, 4]
tp = tuple(tp)
tp
(2, 3, 4)



tp
(2, 3, 4)
# for by value , by index
for value in tp:
    print(value **2)

    
4
9
16
for i in range(len(tp)):
    print(i, tp[i])

    
0 2
1 3
2 4




# dict


di = {}
di
{}
type(di)
<class 'dict'>
di = dict()
di
{}
type(di)
<class 'dict'>



di = {1:"one", 2:"two", 3:"hello", 4:444, 5:(1,2,3,4)}
di
{1: 'one', 2: 'two', 3: 'hello', 4: 444, 5: (1, 2, 3, 4)}
print(di)
{1: 'one', 2: 'two', 3: 'hello', 4: 444, 5: (1, 2, 3, 4)}



di
{1: 'one', 2: 'two', 3: 'hello', 4: 444, 5: (1, 2, 3, 4)}
di[2]
'two'
di[5]
(1, 2, 3, 4)
di[123]
Traceback (most recent call last):
  File "<pyshell#267>", line 1, in <module>
    di[123]
KeyError: 123
di = {1:"one", 2:"two", "333":123124, (2,3):"tuple"}
di
{1: 'one', 2: 'two', '333': 123124, (2, 3): 'tuple'}
di[(2,3)]
'tuple'
di["333"]
123124
di[2]
'two'
di = {[1,2,3]:10,}
Traceback (most recent call last):
  File "<pyshell#273>", line 1, in <module>
    di = {[1,2,3]:10,}
TypeError: unhashable type: 'list'
di = {{1,2,3}:10,}
Traceback (most recent call last):
  File "<pyshell#274>", line 1, in <module>
    di = {{1,2,3}:10,}
TypeError: unhashable type: 'set'



hash
<built-in function hash>
help(hash)
Help on built-in function hash in module builtins:

hash(obj, /)
    Return the hash value for the given object.

    Two objects that compare equal must also have the same hash value, but the
    reverse is not necessarily true.

hash(2)
2
hash("234")
6200312811693258665
hash("234")
6200312811693258665
hash(3.4)
922337203685477379
hash(3.4)

922337203685477379
di = {2:222, 2:2222, 2:22222}
di
{2: 22222}
hash(1)
1
hash(0)
0
hash("")
0
hash(False)
0
hash(True)
1



di = {1:111}
di[1]
111
di[True]
111
hash(())
5740354900026072187



hash(0)
0
hash("")
0
du = {1:111, 0:12345132}
du[0]
12345132
du[False]
12345132
di[""]
Traceback (most recent call last):
  File "<pyshell#307>", line 1, in <module>
    di[""]
KeyError: ''
di = {1:111, 0:12345132, "":"empty"}
di[0]
12345132
di[""]
'empty'
di[False]
12345132




di
{1: 111, 0: 12345132, '': 'empty'}
di.get("")
'empty'
di.get(123123)
di.values()
dict_values([111, 12345132, 'empty'])
di.items()
dict_items([(1, 111), (0, 12345132), ('', 'empty')])
di.keys()
dict_keys([1, 0, ''])
di
{1: 111, 0: 12345132, '': 'empty'}
di.popitem()
('', 'empty')
di
{1: 111, 0: 12345132}
di.pop(0)
12345132
di
{1: 111}
di.update({11:11111})
di
{1: 111, 11: 11111}
di.update({1:-1})
di
{1: -1, 11: 11111}
di
{1: -1, 11: 11111}
1 in di
True
11 in di
True
12 in di
False
di = {1:111, 0:12345132, "":"empty"}



for key in di.keys():
    print(key)

    
1
0

for key in di.values():
    print(key)

    
111
12345132
empty
for key, value in di.items():
    print(key, value)

    
1 111
0 12345132
 empty




di = {str(i):i**3 for i in range(10)}

di
{'0': 0, '1': 1, '2': 8, '3': 27, '4': 64, '5': 125, '6': 216, '7': 343, '8': 512, '9': 729}




# sudents avg


()
()
score = ()
score
()
6
6
score += (6, )
score
(6,)
9
9
score += (9, )
score
(6, 9)
score += (10, )
score
(6, 9, 10)
sum(score)
25
len(score)
3
sum(score)/len(score)
8.333333333333334
(sum(score)/len(score)).round(2)
Traceback (most recent call last):
  File "<pyshell#374>", line 1, in <module>
    (sum(score)/len(score)).round(2)
AttributeError: 'float' object has no attribute 'round'
round
<built-in function round>
round((sum(score)/len(score)), 2)
8.33


def avg(score):
    """функция для вычисления среднего балла студента.
    Arguments:
    score - tuple - набор оценок.
    Returns:
    float - средний балл,  2 знака после запятой.
    """
    return round((sum(score)/len(score)), 2)

score
(6, 9, 10)
avg(score)
8.33


students_grades = {}
def new_grade(students_name):
     """функция для добавления новой оценки студента.
    Arguments:
    students_name - str - имя, не менее 2-х символов.
    Returns:
    True - если оценка добавлена успешно.
    False - если имя менье 2 символов.
    """
    if len(students_name) < 2:
        
SyntaxError: unindent does not match any outer indentation level
def new_grade(students_name):
     """функция для добавления новой оценки студента.
    Arguments:
    students_name - str - имя, не менее 2-х символов.
    Returns:
    True - если оценка добавлена успешно.
    False - если имя менье 2 символов.
    """
    if len(students_name) < 2:
        
SyntaxError: unindent does not match any outer indentation level
def new_grade(students_name, grade):
    """функция для добавления новой оценки студента.
    Arguments:
    students_name - str - имя, не менее 2-х символов.
    grade - int, mark
    Returns:
    True - если оценка добавлена успешно.
    False - если имя менье 2 символов.
    """
    if len(students_name) < 2:
        return False
    students_name = students_name.title()
    if students_name in students_grades:
        students_grades.update(students_grades.get(students_name) + (grade, ))
    else:
        students_grades.update({students_name:(grade, )})
    return True

students_grades
{}
new_grade("Петя петров", 7)
True
students_grades
{'Петя Петров': (7,)}
new_grade("Петя петров", 10)
Traceback (most recent call last):
  File "<pyshell#405>", line 1, in <module>
    new_grade("Петя петров", 10)
  File "<pyshell#401>", line 14, in new_grade
    students_grades.update(students_grades.get(students_name) + (grade, ))
TypeError: cannot convert dictionary update sequence element #0 to a sequence
def new_grade(students_name, grade):
    """функция для добавления новой оценки студента.
    Arguments:
    students_name - str - имя, не менее 2-х символов.
    grade - int, mark
    Returns:
    True - если оценка добавлена успешно.
    False - если имя менье 2 символов.
    """
    if len(students_name) < 2:
        return False
    students_name = students_name.title()
    if students_name in students_grades:
        students_grades.update({students_name: students_grades.get(students_name) + (grade, )})
    else:
        students_grades.update({students_name:(grade, )})
    return True

new_grade("Петя петров", 10)
True
students_grades
{'Петя Петров': (7, 10)}
new_grade("Петя петров", 6)
True
students_grades
{'Петя Петров': (7, 10, 6)}
avg(students_grades.get('Петя Петров'))
7.67

operation = input("1 - new grade, 2 - show avg, 3 - show grades, quit - exit from programm")
1 - new grade, 2 - show avg, 3 - show grades, quit - exit from programm1
def show_grades():
    print("show grades")
    for key, value in students_grades.items():
        print("name:", key)
        print("grades:", value)

        
show_grades()
show grades
name: Петя Петров
grades: (7, 10, 6)
def show_avg():
    print("show avg")
    for key, value in students_grades.items():
        print("name:", key)
        print("avg:", avg(value))

        
show_avg
<function show_avg at 0x000001D284363920>
show_avg()
show avg
name: Петя Петров
avg: 7.67
while operation != "quit":
    match operation:
        case "1":
            name = input("Put name:")
            grade = int(input("Put grade:"))
            new_grade(name, grade)
        case "2":
            show_avg()
        case "3":
            show_grades()
        case _:
            print("Sorry ne ponal")
    operation = input("1 - new grade, 2 - show avg, 3 - show grades, quit - exit from programm")

    
Put name:Вася сидоров
Put grade:9
True
1 - new grade, 2 - show avg, 3 - show grades, quit - exit from programm3
show grades
name: Петя Петров
grades: (7, 10, 6)
name: Вася Сидоров
grades: (9,)
1 - new grade, 2 - show avg, 3 - show grades, quit - exit from programm1
Put name:Вася Сидоров
Put grade:7
True
1 - new grade, 2 - show avg, 3 - show grades, quit - exit from programm3
show grades
name: Петя Петров
grades: (7, 10, 6)
name: Вася Сидоров
grades: (9, 7)
1 - new grade, 2 - show avg, 3 - show grades, quit - exit from programm2
show avg
name: Петя Петров
avg: 7.67
name: Вася Сидоров
avg: 8.0
1 - new grade, 2 - show avg, 3 - show grades, quit - exit from programmquit
def main():
    operation = input("1 - new grade, 2 - show avg, 3 - show grades, quit - exit from programm")
    while operation != "quit":
        match operation:
            case "1":
                name = input("Put name:")
                grade = int(input("Put grade:"))
                new_grade(name, grade)
            case "2":
                show_avg()
            case "3":
                show_grades()
            case _:
                print("Sorry ne ponal")
        operation = input("1 - new grade, 2 - show avg, 3 - show grades, quit - exit from programm")

        
main()
1 - new grade, 2 - show avg, 3 - show grades, quit - exit from programmquit
main()
1 - new grade, 2 - show avg, 3 - show grades, quit - exit from programm3
show grades
name: Петя Петров
grades: (7, 10, 6)
name: Вася Сидоров
grades: (9, 7)
1 - new grade, 2 - show avg, 3 - show grades, quit - exit from programm1
Put name:петя петоров
Put grade:8
1 - new grade, 2 - show avg, 3 - show grades, quit - exit from programm3
show grades
name: Петя Петров
grades: (7, 10, 6)
name: Вася Сидоров
grades: (9, 7)
name: Петя Петоров
grades: (8,)
1 - new grade, 2 - show avg, 3 - show grades, quit - exit from programm2
show avg
name: Петя Петров
avg: 7.67
name: Вася Сидоров
avg: 8.0
name: Петя Петоров
avg: 8.0
1 - new grade, 2 - show avg, 3 - show grades, quit - exit from programmquit










# todo list
# task task_id status
task_list = {}
# task_list[task_id] = {"task_name":"task_name", "status":status-bool}
di = {}
di[1] = {"task_name":"go to school", "status":False}
di
{1: {'task_name': 'go to school', 'status': False}}
di[1]
{'task_name': 'go to school', 'status': False}
di[1]['task_name']
'go to school'
di[1]['status']
False

task_auto_id = 1
def create_task():
    t_name = input("Дай имя задачи:")
    t_status = False
    task_list[task_auto_id] = {"task_name":t_name, "status":False}
    return True

task_list
{}
create_task()
Дай имя задачи:sdfdsfsfsfs
True
task_list
{1: {'task_name': 'sdfdsfsfsfs', 'status': False}}
task_auto_id
1
def create_task():
    t_name = input("Дай имя задачи:")
    task_list[task_auto_id] = {"task_name":t_name, "status":False}
    task_auto_id += 1
    return True

create_task()
Дай имя задачи:dasdsadsad
Traceback (most recent call last):
  File "<pyshell#482>", line 1, in <module>
    create_task()
  File "<pyshell#481>", line 3, in create_task
    task_list[task_auto_id] = {"task_name":t_name, "status":False}
UnboundLocalError: cannot access local variable 'task_auto_id' where it is not associated with a value
def create_task():
    global task_auto_id
    t_name = input("Дай имя задачи:")
    task_list[task_auto_id] = {"task_name":t_name, "status":False}
    task_auto_id += 1
    return True

create_task()
Дай имя задачи:sdasdasdad
True
create_task()gfhfghfhfhg
SyntaxError: invalid syntax
create_task()dfsdfsdfsdf
SyntaxError: invalid syntax
create_task()
Дай имя задачи:fdgdfgdgfdg
True
create_task()
Дай имя задачи:tyrtyryryr
True
task_list
{1: {'task_name': 'sdasdasdad', 'status': False}, 2: {'task_name': 'fdgdfgdgfdg', 'status': False}, 3: {'task_name': 'tyrtyryryr', 'status': False}}
def show_tasks():
    print("show tasks")
    for task_id, description in task_list.items():
        print("_________")
        print("Task id:{task_id}")
        for key, value in description.items:
            print("\t"key, value)
        print("_________")
        
SyntaxError: invalid syntax. Perhaps you forgot a comma?

def show_tasks():
    print("show tasks")
    for task_id, description in task_list.items():
        print("_________")
        print(f"Task id:{task_id}")
        for key, value in description.items:
            print("\t",key, value)
        print("_________")

        
show_tasks()
show tasks
_________
Task id:1
Traceback (most recent call last):
  File "<pyshell#502>", line 1, in <module>
    show_tasks()
  File "<pyshell#501>", line 6, in show_tasks
    for key, value in description.items:
TypeError: 'builtin_function_or_method' object is not iterable
def show_tasks():
    print("show tasks")
    for task_id, description in task_list.items():
        print("_________")
        print(f"Task id:{task_id}")
        for key, value in description.items():
            print("\t",key, value)
        print("_________")

        
show_tasks()
show tasks
_________
Task id:1
	 task_name sdasdasdad
	 status False
_________
_________
Task id:2
	 task_name fdgdfgdgfdg
	 status False
_________
_________
Task id:3
	 task_name tyrtyryryr
	 status False
_________
def change_status():
    task_id = int(input("Дай мне номер задачи:"))
    if task_id not in task_list:
        return False
    inside = task_list.get(task_id)
    inside["status"] = True
    task_list.update({task_id:inside})

    
show_tasks()

show tasks
_________
Task id:1
	 task_name sdasdasdad
	 status False
_________
_________
Task id:2
	 task_name fdgdfgdgfdg
	 status False
_________
_________
Task id:3
	 task_name tyrtyryryr
	 status False
_________
change_status()
Дай мне номер задачи:5
False
change_status()
Дай мне номер задачи:3
show_tasks()
show tasks
_________
Task id:1
	 task_name sdasdasdad
	 status False
_________
_________
Task id:2
	 task_name fdgdfgdgfdg
	 status False
_________
_________
Task id:3
	 task_name tyrtyryryr
	 status True
_________
def main():
    msg = """1 - new task
2 - show tasks
3 - change task status
quit - exit from programm"""
    operation = input(msg)
    while operation != "quit":
        match operation:
            case "1":
                create_task()
            case "2":
                show_tasks()
            case "3":
                change_status()
            case _:
                print("Sorry ne ponal")
        operation = input(msg)

        
main()
1 - new task
2 - show tasks
3 - change task status
quit - exit from programm2
show tasks
_________
Task id:1
	 task_name sdasdasdad
	 status False
_________
_________
Task id:2
	 task_name fdgdfgdgfdg
	 status False
_________
_________
Task id:3
	 task_name tyrtyryryr
	 status True
_________
1 - new task
2 - show tasks
3 - change task status
quit - exit from programm1
Дай имя задачи:dsdfsdfs
1 - new task
2 - show tasks
3 - change task status
quit - exit from programm2
show tasks
_________
Task id:1
	 task_name sdasdasdad
	 status False
_________
_________
Task id:2
	 task_name fdgdfgdgfdg
	 status False
_________
_________
Task id:3
	 task_name tyrtyryryr
	 status True
_________
_________
Task id:4
	 task_name dsdfsdfs
	 status False
_________
1 - new task
2 - show tasks
3 - change task status
quit - exit from programm3
Дай мне номер задачи:4
1 - new task
2 - show tasks
3 - change task status
quit - exit from programm2
show tasks
_________
Task id:1
	 task_name sdasdasdad
	 status False
_________
_________
Task id:2
	 task_name fdgdfgdgfdg
	 status False
_________
_________
Task id:3
	 task_name tyrtyryryr
	 status True
_________
_________
Task id:4
	 task_name dsdfsdfs
	 status True
_________
1 - new task
2 - show tasks
3 - change task status
quit - exit from programmquit



import calendar as c
c.islesp(2000)
Traceback (most recent call last):
  File "<pyshell#524>", line 1, in <module>
    c.islesp(2000)
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python313\Lib\calendar.py", line 56, in __getattr__
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")
AttributeError: module 'calendar' has no attribute 'islesp'. Did you mean: 'isleap'?
>>> c.isleap(2000)
True
>>> c.isleap(2001)
False
>>> c.isleap(2016)
True
>>> c.isleap(2018)
False
>>> import random as r
>>> r.randint(1, 5)
2
>>> r.randint(1, 5)
... 
4
>>> r.randint(1, 5)
... 
3
>>> r.randint(1, 5)
... 
5
>>> r.randint(1, 5)
... 
1
>>> r.randint(1, 5)
... 
4
>>> 
>>> 
>>> 
>>> secret = r.randint(1, 5)
>>> my_number = int(input("дай число от 1-5"))
дай число от 1-54
>>> my_number == secret
True
