# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [58, 2, 29]


def func2():
    return 64.42


def func3():
    return 41


def func4():
    return {'kowie': 18, 'lfbyc': 14, 'obrhc': 59}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
