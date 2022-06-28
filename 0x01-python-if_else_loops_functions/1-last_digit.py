#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    numbers = number * -1
    numbers = numbers % 10
    numbers = numbers * -1
else:
    numbers = number
    numbers = numbers % 10

if numbers < 6 and numbers != 0:
    print(f"Last digit of {number}  is {numbers} and is less than 6 and not 0")
if numbers > 5 and numbers != 0:
    print(f"Last digit of {number}  is {numbers} and is greater than 5")
if numbers == 0:
    print(f"Last digit of {number}  is {numbers} and is 0")
