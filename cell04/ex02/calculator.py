#!/usr/bin/env python3

try:
    num1 = int(input("Give me the first number: "))
    num2 = int(input("Give me the second number: "))
    print("Thank you!")
    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 // num2}")  
    else:
        print("Division by zero is undefined.")
    print(f"{num1} * {num2} = {num1 * num2}")

except ValueError:
    print("Invalid input! Please enter whole numbers only.")