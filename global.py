""" Declare two global variables a and b inside a function that returns the average of a and b
    modify the variables from outside the function"""

from statistics import mean
def get_avg():
    """Gets the average of two global variable a and b"""
    global a
    global b

    return mean([a, b])

a = int(input("input a: "))
b = int(input("Input b: "))

print(get_avg())
