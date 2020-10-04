#!/usr/bin/env python3

import math

name = input("What is your name? ")

birthdate = input("What is your birthdate? ")

age =int(input("How old are you? "))/2

print(f"{name} was born on {birthdate}.")
print("Half of your age is", str(int(math.floor(age))) + ".")



