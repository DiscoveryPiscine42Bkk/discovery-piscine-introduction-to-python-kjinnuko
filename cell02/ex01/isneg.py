#!/usr/bin/env python3

try:
    num = int(input())
    if num < 0:
        print("This number is negative.")
    elif num > 0:
        print("This number is positive.")
    else:
        print("This number is both positive and negative.")
except ValueError:
    print("Not a number, please enter a number.")