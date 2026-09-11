temperature = float(input("What temperature is absolute zero "))
if temperature > 0:
    raise ValueError("The temperature has to be negative")
else:
    print("The temperature is negative, yes, -459.67 F to be exact.")