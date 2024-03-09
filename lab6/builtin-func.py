import math
import time

# 1 Write a Python program with builtin function to multiply all the numbers in a list
def multiply_list(lst: list):
    return math.prod(lst)
# print(multiply_list([1, 2, 3, 4, 5]))

# 2 Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
def count_case(s: str):
    upper = sum(1 for char in s if char.isupper())
    lower = sum(1 for char in s if char.islower())
    return upper, lower
# print(count_case("Hello World"))

# 3 Write a Python program with builtin function that checks whether a passed string is palindrome or not.
def is_palindrome(s: str):
    return s == s[::-1]
# print(is_palindrome("kek"))

# 4 Write a Python program that invoke square root function after specific milliseconds.
def delayed_sqrt(number: int, milliseconds: int):
    time.sleep(milliseconds / 1000)
    return math.sqrt(number)
number = 25100
milliseconds = 2123
# print(f"Square root of {number} after {milliseconds} milliseconds is {delayed_sqrt(number, milliseconds)}")

# 5 Write a Python program with builtin function that returns True if all elements of the tuple are true.
def all_true(t):
    return all(t)
# print(all_true((True, True, True)))
