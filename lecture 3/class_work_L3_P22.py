Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

res_list = list(set(my_list))
res_list
[1, 2, 4, 6, 9]



my_list
[1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
result_list = []

for val in my_list:
    result_list.append(val ** 2)

    
result_list
[1, 4, 16, 16, 1, 16, 4, 36, 4, 81]
result_list = []

for val in my_list:
    if val % 2 == 0:
        result_list.append(val ** 2)

        
result_list
[4, 16, 16, 16, 4, 36, 4]

my_list
[1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
result_list = [val ** 2 for val in my_list]
result_list
[1, 4, 16, 16, 1, 16, 4, 36, 4, 81]
result_list = [val for val in my_list]
result_list
[1, 2, 4, 4, 1, 4, 2, 6, 2, 9]



# n = кол-во чисел. number --> list


res_list = [ int(input("number="))for i in range(int(input("n=")))]
n=5
number=22
number=33
number=44
number=55
number=66
>>> res_list
[22, 33, 44, 55, 66]
>>> 
>>> 
>>> res_list = [ i for i in range(int(input("n="))) if i % 2 == 0]
n=5
>>> res_list
[0, 2, 4]
>>> 
>>> 
>>> 
>>> my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
>>> res_list = {i for i in my_list}
>>> res_list
{1, 2, 4, 6, 9}
>>> res_list = list(set(my_list))
>>> res_list
[1, 2, 4, 6, 9]
>>> 
>>> 
>>> li = [[1,2,3], [3,4,5], [5,6,7]]
>>> len(li)
3
>>> li[0]
[1, 2, 3]
>>> li[1]
[3, 4, 5]
>>> li [0][1]
2
>>> li[1][2]
5
>>> li[2][2]
7
