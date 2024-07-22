# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (60, 42, 38)


def func2():
    return 43.4


def func3():
    return {'wzhdg': 38, 'uwhhz': 24, 'ziwuh': 81}


def func4():
    return 'ctkrw'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
