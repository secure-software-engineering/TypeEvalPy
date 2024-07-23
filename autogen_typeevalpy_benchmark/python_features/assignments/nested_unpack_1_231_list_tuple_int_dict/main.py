# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [49, 93, 4]


def func2():
    return (7, 97, 5)


def func3():
    return 18


def func4():
    return {'yybym': 76, 'njhnm': 77, 'jfpjo': 63}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
