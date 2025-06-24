#!/usr/bin/env python3

try:
    num = int(input("Enter a number\n"))

    i = 0
    while i < 10:
        print(f"{i} x {num} = {i * num}")
        i += 1

except ValueError:
    print("Invalid input! Please enter a valid number.")
