# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [81, 52, 56]


def func2():
    return 'ikdas'


def func3():
    return 7.26


def func4():
    return {'tbwjn': 96, 'hrphy': 51, 'jvaef': 70}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
