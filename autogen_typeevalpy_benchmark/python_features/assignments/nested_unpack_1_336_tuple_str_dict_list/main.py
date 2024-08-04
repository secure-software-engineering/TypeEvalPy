# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (70, 41, 26)


def func2():
    return 'kgnro'


def func3():
    return {'wqnem': 8, 'rvygq': 67, 'vwxys': 26}


def func4():
    return [47, 60, 19]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
