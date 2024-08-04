# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'bvfjt': 58, 'wcbyy': 61, 'wvasc': 3}


def func2():
    return 33.86


def func3():
    return 95


def func4():
    return (69, 28, 27)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
