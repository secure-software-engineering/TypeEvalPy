# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'eduiw': 5, 'shcwj': 100, 'vhnej': 26}


def func2():
    return 'xlamn'


def func3():
    return [25, 44, 62]


def func4():
    return 94


(a, b), (c, d) = [(func1, func2), (func3, func4)]
