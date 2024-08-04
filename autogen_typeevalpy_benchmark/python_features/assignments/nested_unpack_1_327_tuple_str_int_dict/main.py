# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (2, 87, 63)


def func2():
    return 'rknrd'


def func3():
    return 51


def func4():
    return {'kpcyz': 75, 'bzipz': 76, 'dvshs': 35}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
