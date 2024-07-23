# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [59, 24, 64]


def func2():
    return {'shzvx': 46, 'uydtm': 46, 'eeszy': 36}


def func3():
    return 'joyah'


def func4():
    return 87.34


(a, b), (c, d) = [(func1, func2), (func3, func4)]
