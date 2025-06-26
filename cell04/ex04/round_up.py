#!/usr/bin/env python3

import math

try:
    num = float(input("Give me a number: "))
    rounded = math.ceil(num)  # ปัดขึ้น
    print(rounded)
except ValueError:
    print("Invalid input! Please enter a valid number.")