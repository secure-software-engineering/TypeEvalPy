# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'wqdbp': 19, 'gsxuf': 60, 'gsgfm': 47}


def func2():
    return (51, 61, 35)


def func3():
    return 'bvgwd'


def func4():
    return 90


(a, b), (c, d) = [(func1, func2), (func3, func4)]
