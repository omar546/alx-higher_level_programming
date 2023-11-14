#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
last_digit_int = int(last_digit)
st = "Last digit of"
if number < 0:
    last_digit = -last_digit
if last_digit > 5:
    st2 = "and is greater than 5"
elif last_digit == 0:
    st2 = "and is 0"
elif last_digit < 6:
    st2 = "and is less than 6 and not 0"
print(f"{st} {number:d} is {last_digit} {st2}")
