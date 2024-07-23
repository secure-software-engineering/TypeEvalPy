# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [98, 6, 23]


def func2():
    return (78, 14, 84)


def func3():
    return {'xbrgc': 83, 'dfxyq': 68, 'cokaf': 38}


def func4():
    return 'reurb'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
