def change(func):
    print("Decor eat name func")
    def inner(inner_number):
        print("вместо оригинала запущенна иннер функция")
        return func(inner_number*2)
    return inner


@change
def sub_five(number):
    print("и только тут я вызвал оригинальную функцию add_five")
    return number - 5


@change
def add_five(number):
    print("и только тут я вызвал оригинальную функцию add_five")
    return number + 5


print(add_five(6))
print(sub_five(6))
