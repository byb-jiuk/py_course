Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
li = [1, 2, 3, 4, 5, 5]
li
[1, 2, 3, 4, 5, 5]

new_list = li
new_list
[1, 2, 3, 4, 5, 5]
new_list[1]
2
new_list[1]= 99
new_list
[1, 99, 3, 4, 5, 5]
li
[1, 99, 3, 4, 5, 5]
id
<built-in function id>
help(id)
Help on built-in function id in module builtins:

id(obj, /)
    Return the identity of an object.

    This is guaranteed to be unique among simultaneously existing objects.
    (CPython uses the object's memory address.)

id(new_list)
     
1973188738048
id(li)
     
1973188738048
li = [1, 2, 3, 4, 5, 5]

li = [1, 2, 3, 4, 5, 5]
     
new_list= li.copy()
     
li
     
[1, 2, 3, 4, 5, 5]
new_list
     
[1, 2, 3, 4, 5, 5]
id(new_list)
     
1973144958784
id(li)
     
1973188757376
new_list[1] = 999
     
new_list
     
[1, 999, 3, 4, 5, 5]


new_list = li[:]
     
id(new_list)
     
1973188738048
id(li)
     
1973188757376
li = [1, 2, 3, 4, 5, 5]
     
kkk = [1,2,3,4, li]
     
kkk
     
[1, 2, 3, 4, [1, 2, 3, 4, 5, 5]]
new_list = kkk[:]
     
id(kkk)
     
1973188863168
id(new_list)
     
1973188757376


li[0] = 1000
     
kkk
     
[1, 2, 3, 4, [1000, 2, 3, 4, 5, 5]]
new_list
     
[1, 2, 3, 4, [1000, 2, 3, 4, 5, 5]]
new_list[0] = 999
     
new_list
     
[999, 2, 3, 4, [1000, 2, 3, 4, 5, 5]]
kkk
     
[1, 2, 3, 4, [1000, 2, 3, 4, 5, 5]]



from copy import deepcopy
     
help(deepcopy)
     
Help on function deepcopy in module copy:

deepcopy(x, memo=None, _nil=[])
    Deep copy operation on arbitrary Python objects.

    See the module's __doc__ string for more info.

li = [1, 2, 3, 4, 5, 5]
     
kkk = [1,2,3,4, li]
     
new_list = deepcopy(kkk)
     
li[0] = 5555
     
li
     
[5555, 2, 3, 4, 5, 5]
kkk
     
[1, 2, 3, 4, [5555, 2, 3, 4, 5, 5]]
new_list
     
[1, 2, 3, 4, [1, 2, 3, 4, 5, 5]]








#strimg
     
st="12345dfasdfasfd"
     
s2 = "asdasdasdas"
     
s3 = "name DOme No"
     
print(st)
     
12345dfasdfasfd
print(s2)
     
asdasdasdas
print(s3)
     
name DOme No
print(repr()st)
     
SyntaxError: invalid syntax. Perhaps you forgot a comma?
len(st)
     
15
len(s2)
     
11
len(s3)
     
12


a = "hello"
     
b = "Hello"
     
c = "hello"
     
a == b
     
False
a == c
     
True

a = "asdsdasd"
     
b = 'asdsad'
     
a
     
'asdsdasd'
b
     
'asdsad'


a
     
'asdsdasd'
a += b
     
a
     
'asdsdasdasdsad'
a = a + b
     
a
     
'asdsdasdasdsadasdsad'
a * 9
     
'asdsdasdasdsadasdsadasdsdasdasdsadasdsadasdsdasdasdsadasdsadasdsdasdasdsadasdsadasdsdasdasdsadasdsadasdsdasdasdsadasdsadasdsdasdasdsadasdsadasdsdasdasdsadasdsadasdsdasdasdsadasdsad'
9 * a
     
'asdsdasdasdsadasdsadasdsdasdasdsadasdsadasdsdasdasdsadasdsadasdsdasdasdsadasdsadasdsdasdasdsadasdsadasdsdasdasdsadasdsadasdsdasdasdsadasdsadasdsdasdasdsadasdsadasdsdasdasdsadasdsad'
a
     
'asdsdasdasdsadasdsad'
a *=3
     
a
     
'asdsdasdasdsadasdsadasdsdasdasdsadasdsadasdsdasdasdsadasdsad'
a = a *3
     
a
     
'asdsdasdasdsadasdsadasdsdasdasdsadasdsadasdsdasdasdsadasdsadasdsdasdasdsadasdsadasdsdasdasdsadasdsadasdsdasdasdsadasdsadasdsdasdasdsadasdsadasdsdasdasdsadasdsadasdsdasdasdsadasdsad'

ord
     
<built-in function ord>
chr
     
<built-in function chr>
help(chr)
     
Help on built-in function chr in module builtins:

chr(i, /)
    Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.

help(ord)
     
Help on built-in function ord in module builtins:

ord(c, /)
    Return the Unicode code point for a one-character string.

"a"
     
'a'
a
     
'asdsdasdasdsadasdsadasdsdasdasdsadasdsadasdsdasdasdsadasdsadasdsdasdasdsadasdsadasdsdasdasdsadasdsadasdsdasdasdsadasdsadasdsdasdasdsadasdsadasdsdasdasdsadasdsadasdsdasdasdsadasdsad'
a = "a"
     
ord(a)
     
97
ord("D")
     
68
ord("S")
     
83
ord("+")
     
43
ord("П")
     
1055
ord("~")
     
126
chr(1000)
     
'Ϩ'
chr(1001)
     
'ϩ'
chr(10005)
     
'✕'
for i in range (2500, 2600):
     print(chr(i), end="")

     
ৄ৅৆েৈ৉৊োৌ্ৎ৏৐৑৒৓৔৕৖ৗ৘৙৚৛ড়ঢ়৞য়ৠৡৢৣ৤৥০১২৩৪৫৬৭৮৯ৰৱ৲৳৴৵৶৷৸৹৺৻ৼ৽৾৿਀ਁਂਃ਄ਅਆਇਈਉਊ਋਌਍਎ਏਐ਑਒ਓਔਕਖਗਘਙਚਛਜਝਞਟਠਡਢਣਤਥਦਧ
for i in range (3500, 3600):
     print(chr(i), end="")

     
ඬතථදධන඲ඳපඵබභමඹයර඼ල඾඿වශෂසහළෆ෇෈෉්෋෌෍෎ාැෑිීු෕ූ෗ෘෙේෛොෝෞෟ෠෡෢෣෤෥෦෧෨෩෪෫෬෭෮෯෰෱ෲෳ෴෵෶෷෸෹෺෻෼෽෾෿฀กขฃคฅฆงจฉชซฌญฎฏ
for i in range (22500, 22600):
     print(chr(i), end="")

     
埤埥埦埧埨埩埪埫埬埭埮埯埰埱埲埳埴埵埶執埸培基埻埼埽埾埿堀堁堂堃堄堅堆堇堈堉堊堋堌堍堎堏堐堑堒堓堔堕堖堗堘堙堚堛堜堝堞堟堠堡堢堣堤堥堦堧堨堩堪堫堬堭堮堯堰報堲堳場堵堶堷堸堹堺堻堼堽堾堿塀塁塂塃塄塅塆塇
s = "埤埥埦埧埨埩埪埫埬埭埮埯埰埱埲埳埴埵埶執埸培基埻埼埽埾埿堀堁堂堃堄堅堆堇堈堉堊堋堌堍堎堏堐堑堒堓堔堕堖堗堘堙堚堛堜堝堞堟堠堡堢堣堤堥堦堧堨堩堪堫堬堭堮堯堰報堲堳場堵堶堷堸堹堺堻堼堽堾堿塀塁塂塃塄塅塆塇"
     
for i in s:
     print(ord(i), end="")

     
22500225012250222503225042250522506225072250822509225102251122512225132251422515225162251722518225192252022521225222252322524225252252622527225282252922530225312253222533225342253522536225372253822539225402254122542225432254422545225462254722548225492255022551225522255322554225552255622557225582255922560225612256222563225642256522566225672256822569225702257122572225732257422575225762257722578225792258022581225822258322584225852258622587225882258922590225912259222593225942259522596225972259822599



s = "hello"
     
len(s)
     
5
s[0]
     
'h'
s[4]
     
'o'
s[5]
     
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    s[5]
IndexError: string index out of range
s[0] = "d"
     
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    s[0] = "d"
TypeError: 'str' object does not support item assignment
s
     
'hello'
for letter in s:
     print(letter)

     
h
e
l
l
o
len(5)
     
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    len(5)
TypeError: object of type 'int' has no len()
len(s)
     
5
for i in range(len(s)):
     print(i, s[i])

     
0 h
1 e
2 l
3 l
4 o
li = [1,2,3,4,5,5]
     
li
     
[1, 2, 3, 4, 5, 5]
len(li)
     
6
for i in range(len(li)):
     print(i, li[i])

     
0 1
1 2
2 3
3 4
4 5
5 5






secret_key = 5
     
text = "abcdefgh"
     
# chr ord
     
ord("a")
     
97
97+5
     
102
chr(102)
     
'f'



message = "Привет! Наш гонец отправлен в Филадльфи, чтобы предупредить командрующего петра первого."
     
secured_message = ""
     
secret_key = 5
     
for letter in message:
     secured_message += chr(ord(letter) + secret_key)

     
secured_message
     
'Фхнзкч&%Теэ%иуткы%учфхезркт%з%Щнрейрёщн1%ьчужѐ%фхкйшфхкйнчё%пусетйхшѓюкиу%фкчхе%фкхзуиу3'

# поолучатель
     
secured_message
     
'Фхнзкч&%Теэ%иуткы%учфхезркт%з%Щнрейрёщн1%ьчужѐ%фхкйшфхкйнчё%пусетйхшѓюкиу%фкчхе%фкхзуиу3'
secret_key = 5

result_message = ""
     
for letter in secured_message:
     result_message += chr(ord(letter) - secret_key)

     
result_message
     
'Привет! Наш гонец отправлен в Филадльфи, чтобы предупредить командрующего петра первого.'


s ="hello"
     
s
     
'hello'
s[0]
     
'h'
s[:3]
     
'hel'
s[1:4]
     
'ell'
s[1:]
     
'ello'

s

s
     
'hello'
s[::-1]
     
'olleh'
# string [start:end:step]
     
li = [1,2,3,4,5]
     
li
     
[1, 2, 3, 4, 5]
li[1:4]
     
[2, 3, 4]
li[::1]
     
[1, 2, 3, 4, 5]
s
     
'hello'
s[::2]
     
'hlo'
s[::-1]
     
'olleh'
s[::-3]
     
'oe'
s[0]
     
'h'
s[-1]
     
'o'
s[-3]
     
'l'



s = "a b c d e"
     
s
     
'a b c d e'
len(s)
     
9
s[4]
     
'c'
s[4] = "C"
     
Traceback (most recent call last):
  File "<pyshell#210>", line 1, in <module>
    s[4] = "C"
TypeError: 'str' object does not support item assignment


s[:4]
     
'a b '
"C"
     
'C'
s[5:]
     
' d e'
s
     
'a b c d e'
res_string = s[:4] + "C" + s[5:]
     
res_string
     
'a b C d e'
s
     
'a b c d e'
# in not in
     

"a" in res_string
     
True
" " in res_string
     
True
"c" in res_string
     
False
"b" in res_string
     
True
"C" in res_string
     
True
"C" not in res_string
     
False
"a" not in res_string
     
False



s
     
'a b c d e'
del s
     
s
     
Traceback (most recent call last):
  File "<pyshell#234>", line 1, in <module>
    s
NameError: name 's' is not defined
s = 'a b c d e'
     
min
     
<built-in function min>
max
     
<built-in function max>
li  = [1,2,3,4,5, 66666]
     
li
     
[1, 2, 3, 4, 5, 66666]
max(li)
     
66666
min(li)
     
1
s
     
'a b c d e'
min(s)
     
' '
max(s)
     
'e'
li = []
     
max(li)
     
Traceback (most recent call last):
  File "<pyshell#246>", line 1, in <module>
    max(li)
ValueError: max() iterable argument is empty




s = "hello"
     
s.upper()
     
'HELLO'
s = s.upper()
     
s.lower()
     
'hello'
s = s.lower()
     
s.title()
     
'Hello'
s.capitalize()
     
'Hello'
s = 'hello hello hello'
     
s.title()
     
'Hello Hello Hello'
.capitalize()
     
SyntaxError: invalid syntax
s.swapcase()
     
'HELLO HELLO HELLO'
s
     
'hello hello hello'
s.isalpha()
     
False
s = "asdasdasd"
     
s.isalpha()
     
True
s = "asdasdasd12345"
     
s.isalpha()
     
False
s.isalnum()
     
True
s = "fdsfsfsdf123 "
     
s.isalnum
     
<built-in method isalnum of str object at 0x000001CB6B3A07F0>
ch = " "
     
ch.isspace()
     
True
ch = "H"
     
ch.isspace()
     
False
ch.istitle()
     
True




# name
     


name = input("-->")
     
-->VASIA
name
     
'VASIA'
name.capitalize()
     
'Vasia'
name = name.capitalize()
     
name
     
'Vasia'
name = input("-->").capitalize()
     
-->ptre
name
     
'Ptre'

s = "  peter   "
     
s.capitalize()
     
'  peter   '
s.title()
     
'  Peter   '
s.strip()
     
'peter'
name = input("-->").strip().capitalize()
     
-->              fsdfsfsf
name
     
'Fsdfsfsf'

name.replace("df", "OLD")
     
'FsOLDsfsf'
name
     
'Fsdfsfsf'
name = name.replace("df", "OLD")
     
name
     
'FsOLDsfsf'
url = "https://vk.com/"
     
url = url.replace(".com", ".org")
     
url
     
'https://vk.org/'



numbers = input("-->")
     
-->1 2 3 4 5 6 7 8
>>> numbers
...      
'1 2 3 4 5 6 7 8'
>>> numbers.split()
...      
['1', '2', '3', '4', '5', '6', '7', '8']
>>> numbers=numbers.split()
... 
>>> res_list = []
...      
>>> for i in numbers^
...      
SyntaxError: invalid syntax
>>> for i in numbers:
...      res_list.append(int(i))
... 
...      
>>> res_list
...      
[1, 2, 3, 4, 5, 6, 7, 8]
>>> sum(res_list)
...      
36
>>> nums = [int (snumber) for snumber in input("-->").split()]
...      
-->1 2 3 4 5 6 7 8 9 10
>>> nums
...      
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> sum(nums)
...      
55
>>> max(nums)
...      
10
>>> min(nums)
...      
1
