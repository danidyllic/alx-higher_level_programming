#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    digit = number % 10
else:
    digit = number % -10

if number > 0:
    print("{:d} is positive".format(number))
elif number == 0:
    print("{:d} is zero".format(number))
else:
    print("{:d} is negative".format(number))
    
print("last digit of {} is {}".format(number, digit), end='')

if digit > 5:
    print(" and is greater than 5")
elif digit == 0:
    print(" and is 0")
else:
    print(" and is less than 6 and not 0")
