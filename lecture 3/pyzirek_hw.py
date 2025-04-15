# Home work 3.3 Сортировка пузырьком.
li = [20, 35, 10, 5]  # Необходимо осортировать список след образом [5, 10, 20, 35].
swapped = True

while swapped:
    swapped = False
    for index in range(len(li)-1):
        if li[index] > li[index+1]:  # Проверяем действительно ли [index] > [index+1].
            li[index], li[index + 1] = li[index+1], li[index]  # Если больше производит замену.
            swapped = True

print(li)
