# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [49, 28, 35]


def func2():
    return 6


def func3():
    return {'sumzu': 12, 'ibiac': 55, 'ocmjy': 20}


def func4():
    return 24.5


(a, b), (c, d) = [(func1, func2), (func3, func4)]
