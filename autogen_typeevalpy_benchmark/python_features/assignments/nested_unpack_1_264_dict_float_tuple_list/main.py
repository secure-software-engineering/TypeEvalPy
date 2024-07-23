# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'azvkp': 38, 'apsjn': 78, 'corzp': 33}


def func2():
    return 35.06


def func3():
    return (55, 95, 70)


def func4():
    return [35, 52, 76]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
