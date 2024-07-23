# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 77


def func2():
    return 92.44


def func3():
    return {'trapb': 90, 'ojvgv': 46, 'hsgfy': 48}


def func4():
    return [74, 79, 90]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
