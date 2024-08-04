# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (26, 64, 82)


def func2():
    return 'wuvnh'


def func3():
    return {'bzkft': 39, 'cvcib': 65, 'umfuq': 39}


def func4():
    return 43.86


(a, b), (c, d) = [(func1, func2), (func3, func4)]
