# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'crutw': 50, 'hocop': 22, 'oapsy': 88}


def func2():
    return (19, 86, 85)


def func3():
    return [42, 74, 7]


def func4():
    return 6


(a, b), (c, d) = [(func1, func2), (func3, func4)]
