# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 93


def func2():
    return [55, 44, 10]


def func3():
    return {'ictcv': 29, 'vkqbm': 83, 'tipzo': 73}


def func4():
    return 54.7


(a, b), (c, d) = [(func1, func2), (func3, func4)]
