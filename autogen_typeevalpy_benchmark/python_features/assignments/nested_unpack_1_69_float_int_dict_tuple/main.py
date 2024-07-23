# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 32.01


def func2():
    return 61


def func3():
    return {'kbhct': 35, 'lnoky': 9, 'iqnzo': 11}


def func4():
    return (53, 21, 96)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
