operation = input("+ - * / exit")
while operation != "exit":
    number1 = int(input("Введи число:"))
    number2 = int(input("Введи число:"))
    if operation == "+":
        print (number1 + number2)
    elif operation == "-":
        print (number1 - number2)
    elif operation == "*":
        print (number1 * number2)
    elif operation == "/":
        print (number1 / number2)
    else:
        print ("Dont understand...")
    operation = input("+ - * / exit")