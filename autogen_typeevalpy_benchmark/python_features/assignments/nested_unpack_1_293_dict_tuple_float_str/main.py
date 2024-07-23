# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'islwm': 59, 'agavj': 99, 'ejuft': 40}


def func2():
    return (64, 95, 82)


def func3():
    return 10.65


def func4():
    return 'aance'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
