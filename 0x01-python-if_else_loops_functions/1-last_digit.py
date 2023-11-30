#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10 if number > 10 else number % -10
fstr = "Last digit of {} is {}".format(number, last_digit)
if last_digit > 5:
    print(fstr, "and is greater than 5")
elif last_digit == 0:
    print(fstr, "and is 0")
else:
    print(fstr, "and is less than 6 and not 0")
