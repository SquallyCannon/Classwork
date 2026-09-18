import random
number1 = int(input('Enter your first number '))
number2 = int(input('Enter your second number '))

def calculate(number1, number2):
    operand = random.randint(1,3)
    if operand == 1:
        operator = "+"
        print(number1, "+", number2, "=", number1 + number2)
    elif operand == 2:
        operator = "-"
        print(number1, "-", number2, "=", number1 - number2)
    else:
        operator = "*"
        print(number1, "*", number2, "=", number1 * number2)
    
calculate(number1, number2)