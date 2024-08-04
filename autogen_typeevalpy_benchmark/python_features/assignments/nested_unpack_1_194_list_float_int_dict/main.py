# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [67, 48, 90]


def func2():
    return 11.53


def func3():
    return 22


def func4():
    return {'mvtkg': 87, 'fdwfv': 76, 'eitbq': 16}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
