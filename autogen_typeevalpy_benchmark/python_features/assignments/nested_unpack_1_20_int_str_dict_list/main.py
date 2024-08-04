# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 42


def func2():
    return 'iwhyk'


def func3():
    return {'vmtby': 15, 'fbyba': 73, 'gvqgm': 28}


def func4():
    return [60, 90, 33]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
