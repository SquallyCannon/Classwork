import questionary
import copy
import sys
import math

def fibonacci(terms):
    fiblist = []
    previous1 = 0
    previous2 = 1
    if terms <= 1:
        fiblist = [0]
    else:
        fiblist.append(previous1)
        fiblist.append(previous2)
        for term in range(terms-1):
            temp = previous1 + previous2
            fiblist.append(temp)
            previous1 = copy.copy(previous2)
            previous2 = temp
    result = ", ".join(map(str, fiblist))
    return result

def prime_check(prime):
    primebools = True
    if prime < 2:
        primebools = False
    if primebools == True:
        for number in range(prime):
            if number < 2:
                continue
            if prime % number == 0 and number != prime:
                primebools = False
    return primebools

def prime_list(mini, maxi):
    terms = maxi - mini
    primelist = []
    if terms < 1:
        return print("This range is 0 or less")
    else:
        for term in range(mini, maxi+1):
            primebol = prime_check(term)
            if primebol == True: 
                primelist.append(term)
        result = ", ".join(map(str, primelist))
        return result

def multtable(base, leng):
    for number in range(1, leng+1):
        print(f"{base} x {number} = {base*number}")

def powertable(base, leng):
    for number in range(2, leng+1):
        print(f"{base} ^ {number} = {base**number}")

def terminal(base):
    negative = False
    if base < 0:
        negative = True
    basic = copy.copy(base)
    for number in range(1, abs(basic)):
        base = abs(base) + number
    if negative == True:
        base = -base
    return base

def factorial(base):
    basic = copy.copy(base)
    for number in range(1, abs(basic)):
        base = base * number
    return base

def expfactorial(base):
    exp = 1
    basic = copy.copy(base)
    for number in range(1, abs(basic)):
        exp = number ** exp
    base2 = base ** exp
    if basic >= 5:
        base2 = math.log(base2, 10)
        return f"{math.floor(base2)} digits"
    return base2

def collatz(terms):
    steps = 0
    while terms > 1:
        steps += 1
        if terms % 2 == 0:
            terms /= 2
        elif terms % 2 == 1:
            terms = (terms * 3) + 1
    return steps

operation = True
while operation == True:
    sequence = questionary.select(
        "Please select a sequence:",
        choices=["Fibonacci Numbers", "Check if Prime", "Prime numbers in range", "Multiplication Table", "Power Table", "Terminal", "Factoral", "Exp Factoral", "Collatz Sequence","Exit"],
    ).ask()

    print(f"You selected: {sequence}")
    if sequence == "Fibonacci Numbers":
        looping = True
        while looping == True:
            try:
                terms = int(input("How many terms?: "))
            except:
                print("Fibonacci's must be an integer")
            else:
                validate = questionary.confirm(message=f"Use {terms} for fibonacci?: ").ask()
                if validate == True:
                    print(fibonacci(terms))
                looping = False
    
    elif sequence == "Check if Prime":
        looping = True
        while looping == True:
            try:
                prime = int(input("What number do you want to check?: "))
            except:
                print("Primes's must be an number")
            else:
                validate = questionary.confirm(message=f"Use {prime} for prime check?: ").ask()
                if validate == True:
                    primebool = bool(prime_check(prime))
                    print(primebool)
                    if primebool == True:
                        print(f"{prime} is prime")
                    else:
                        print(f"{prime} is not prime")
                looping = False
    
    elif sequence == "Prime numbers in range":
        looping = True
        while looping == True:
            try:
                mini = int(input("What is the miniimum?: "))
                maxi = int(input("What is the maxiimum?: "))
            except:
                print("Ranges must be an integer")
            else:
                validate = questionary.confirm(message=f"Use {mini} - {maxi} for prime check range?: ").ask()
                if validate == True:
                    print(prime_list(mini, maxi))
                looping = False
                
    elif sequence == "Multiplication Table":
        looping = True
        while looping == True:
            try:
                base = float(input("What is the base?: "))
                leng = int(input("What is the length?: "))
                if base % 1 == 0:
                    base = int(base)
                if leng < 1:
                    raise ValueError
            except:
                print("Lengths must be an positive integer and base must be a number")
            else:
                validate = questionary.confirm(message=f"Use {base} and {leng} for base and length?: ").ask()
                if validate == True:
                    multtable(base, leng)
                looping = False

    elif sequence == "Power Table":
        looping = True
        while looping == True:
            try:
                base = float(input("What is the base?: "))
                leng = int(input("What is the highest power?: "))
                if base % 1 == 0:
                    base = int(base)
                if leng < 1:
                    raise ValueError
            except:
                print("Lengths must be an positive integer and base must be a number")
            else:
                validate = questionary.confirm(message=f"Use {base} and {leng} for base and length?: ").ask()
                if validate == True:
                    powertable(base, leng)
                looping = False

    elif sequence == "Terminal":
        looping = True
        while looping == True:
            try:
                base = int(input("What is the terminal?: "))
            except:
                print("terminal must be an integer.")
            else:
                validate = questionary.confirm(message=f"Use {base} for terminal?: ").ask()
                if validate == True:
                    print(terminal(base))
                looping = False

    elif sequence == "Factoral":
        looping = True
        while looping == True:
            try:
                base = int(input("What is the factorial?: "))
            except:
                print("Factorial must be an integer.")
            else:
                validate = questionary.confirm(message=f"Use {base} for factorial?: ").ask()
                if validate == True:
                    print(factorial(base))
                looping = False

    elif sequence == "Exp Factoral":
        looping = True
        while looping == True:
            try:
                base = int(input("What is the exp factorial?: "))
            except:
                print("Exp factorial must be an integer.")
            else:
                validate = questionary.confirm(message=f"Use {base} for exp factorial?: ").ask()
                if validate == True:
                    print(expfactorial(base))
                looping = False
    
    elif sequence == "Collatz Sequence":
        looping = True
        while looping == True:
            try:
                terms = int(input("What's the starting number?: "))
                if terms < 0:
                    raise ValueError
            except:
                print("Collatz start must be an positive integer.")
            else:
                validate = questionary.confirm(message=f"Use {terms} for Collatz Sequence?: ").ask()
                if validate == True:
                    print(collatz(terms))
                    looping = False

    else:
        operation = False
