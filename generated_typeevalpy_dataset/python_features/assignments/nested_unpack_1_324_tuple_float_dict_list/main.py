# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (33, 61, 80)


def func2():
    return 59.03


def func3():
    return {'fuwfj': 42, 'dtstd': 39, 'dubcv': 49}


def func4():
    return [24, 88, 91]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
