from random import randrange
from random import randint
from random import random
for i in range(10):
    print(randrange(6,20))
for i in range(10):
    print(randint(6,20))
for i in range(10):
    rand = random()
    if rand >= 0.75:
        print("bonus")