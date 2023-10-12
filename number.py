#!/usr/bin/python3
"""Sets 10 elements to 0
    Adds random numbers to these elements
    Prints the elements with the original being the first and the modified being the second
"""
import random
#populating a list with ten 0s using list comprehensions
elements = [0 for i in range(10)]

new_elements = list(map(lambda x: x + random.randint(1, 9), elements))

print(elements)
print(new_elements)
