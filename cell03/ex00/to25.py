#!/usr/bin/env python3

try:
    num = int(input("Enter a number less than 25\n"))

    if num > 25:
        print("Error")
    else:
        while num <= 25:
            print(f"Inside the loop, my variable is {num}")
            num += 1
except ValueError:
    print("Invalid input! Please enter a valid number.")