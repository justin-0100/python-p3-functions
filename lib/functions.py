#!/usr/bin/env python3

# 1. No arguments, just prints
def greet_programmer():
    print("Hello, programmer!")

# 2. One argument, prints personalized greeting
def greet(name):
    print(f"Hello, {name}!")

# 3. One argument with default value
def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

# 4. Adds two numbers and returns result
def add(num1, num2):
    return num1 + num2

# 5. Returns half of the number
def halve(number):
    return number / 2
