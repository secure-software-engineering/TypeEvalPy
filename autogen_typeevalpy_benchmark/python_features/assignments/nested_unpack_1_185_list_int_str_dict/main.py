# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [6, 71, 64]


def func2():
    return 27


def func3():
    return 'rmgac'


def func4():
    return {'comyu': 38, 'bsxql': 47, 'zgbvw': 87}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
