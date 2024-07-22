# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 14.2


def func2():
    return {'lowte': 82, 'zjmyz': 36, 'ltfuz': 41}


def func3():
    return (63, 4, 9)


def func4():
    return 94


(a, b), (c, d) = [(func1, func2), (func3, func4)]
