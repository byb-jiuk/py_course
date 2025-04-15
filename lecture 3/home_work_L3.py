# # Home work 3.3 Сортировка пузырьком.
# li = [20, 35, 10, 5]  # Необходимо осортировать список след образом [5, 10, 20, 35].
# swapped = True

# while swapped:
#     swapped = False
#     for index in range(len(li)-1):
#         if li[index] > li[index+1]:  # Проверяем действительно ли [index] > [index+1].
#             li[index], li[index + 1] = li[index+1], li[index]  # Если больше производит замену.
#             swapped = True

# print(li)  # Выводим отсортированый список





# # Home work 3.5. Программа, которая ввыводит сумму значений списка.
# li = input('put string of numbers by space:').split()  # Вводим значения.
# Li = [int(val) for val in li]  # Создаем список из введенных значений.
# print("after append in list:", Li)  # Выводим список.
# S = sum(Li)  # Задаем переменную с суммой значений списка.
# print("Sum(list):\n", S)  # Печатаем сумму.
