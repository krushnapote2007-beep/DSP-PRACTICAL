# mymodule.py
def add(a, b):
 return a + b
def multiply(a, b):
 return a * b

# mymodule.py
def add1(a, b):
 return a + b
def multiply1(a, b):
 return a * b

import math
print(math.sqrt(25))
print(math.factorial(5))
print(math.ceil(4.3))

import random
print(random.randint(1, 10))
print(random.choice([10, 20, 30]))

import statistics
data = [10, 20, 20, 30]
print(statistics.mean(data))
print(statistics.median(data))
print(statistics.mode(data))

import math
num = 16
print("Square root:", math.sqrt(num))
print("Factorial:", math.factorial(5))
print("Power:", math.pow(2, 3))
print("Log:", math.log(10))

from functools import reduce
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, numbers)
print("Sum using reduce:", result)

import my_module
print("Addition:", my_module.add(5, 3))
print("Multiplication:", my_module.multiply(4, 2))

