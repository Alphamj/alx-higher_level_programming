#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_str1 = repr(number)
last_digit_str = num_str1[-1]
num_str2= int(last_digit_str)
if number < 0:
    num_str = num_str2 - (num_str2 * 2)
else:
    num_str = num_str2
if num_str > 5:
    print(f"Last digit of {number} is {num_str} and is greater than 5")
elif num_str == 0:
    print(f"Last digit of {number} is {num_str} and is 0")
else:
    print(f"Last digit of {number} is {num_str} and is less than 6 and not 0")
