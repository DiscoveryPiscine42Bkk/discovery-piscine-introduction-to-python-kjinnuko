#!/usr/bin/env python3

try:
    num_str = input("Give me a number: ")
    num = float(num_str)
    
    if num.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
        
except ValueError:
    print("Invalid input! Please enter a valid number.")

