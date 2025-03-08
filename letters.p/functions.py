# task 1
from math import prod

def multiply_list(numbers):
    return prod(numbers)

print(multiply_list([1, 2, 3, 4]))

# task 2
def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return {"Uppercase": upper, "Lowercase": lower}

print(count_case("Hello World!"))

# task 3
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("radar"))
print(is_palindrome("hello")) 


# task 4
import time
import math

def delayed_sqrt(number, delay):
    time.sleep(delay / 1000)
    return math.sqrt(number)

# Input
num = 25100
delay_ms = 2123

# Output
result = delayed_sqrt(num, delay_ms)
print(f"Square root of {num} after {delay_ms} milliseconds is {result}")

# task 5 
def all_true(t):
    return all(t)

print(all_true((True, True, True)))  
print(all_true((True, False, True)))

24
{'Uppercase': 2, 'Lowercase': 8}
True
False
Square root of 25100 after 2123 milliseconds is 158.42979517754858
True
False

