# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (21, 9, 31)


def func2():
    return 28


def func3():
    return 38.28


def func4():
    return {'kbzgq': 62, 'zdzxs': 29, 'norot': 99}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
