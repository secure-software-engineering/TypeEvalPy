# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 63


def func2():
    return {'bfwej': 2, 'uqwtp': 44, 'zwcjs': 15}


def func3():
    return (16, 53, 51)


def func4():
    return [16, 16, 41]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
