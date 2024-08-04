# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 53.29


def func2():
    return {'jxcvx': 8, 'fnewl': 59, 'rsmxl': 17}


def func3():
    return 'nlbmu'


def func4():
    return (93, 3, 51)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
