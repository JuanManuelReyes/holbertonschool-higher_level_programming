#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number > 0:
    aux = number % 10

else:
    aux = number % -10

if aux > 5:
    print(f"Last digit of {number} is {aux} and is greater than 5")
elif aux == 0:
     print(f"Last digit of {number} is {aux} and is 0")
else:
     print(f"Last digit of {number} is {aux} and is less than 6 and not 0")
