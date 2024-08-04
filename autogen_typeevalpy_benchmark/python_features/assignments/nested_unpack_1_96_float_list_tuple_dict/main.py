# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 98.24


def func2():
    return [99, 37, 91]


def func3():
    return (27, 89, 91)


def func4():
    return {'mmoys': 11, 'hooxk': 45, 'iudby': 57}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
