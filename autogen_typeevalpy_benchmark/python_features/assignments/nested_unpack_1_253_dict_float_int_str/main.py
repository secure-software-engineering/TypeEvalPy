# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'niizv': 92, 'xaewv': 36, 'mhwnd': 70}


def func2():
    return 30.06


def func3():
    return 51


def func4():
    return 'ufarx'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
