# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [85, 83, 64]


def func2():
    return (91, 77, 37)


def func3():
    return {'cqwwb': 52, 'uxrbn': 32, 'vvsjb': 49}


def func4():
    return 'paocl'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
