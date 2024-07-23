# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'kusvk'


def func2():
    return {'idpit': 89, 'vcvpf': 7, 'oiptc': 90}


def func3():
    return 72


def func4():
    return [61, 44, 21]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
