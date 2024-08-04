# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'wiiuc': 77, 'znzfa': 12, 'kwdib': 43}


def func2():
    return 'mbnri'


def func3():
    return [74, 98, 40]


def func4():
    return 64.25


(a, b), (c, d) = [(func1, func2), (func3, func4)]
