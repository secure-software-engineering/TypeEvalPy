# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'posnc': 17, 'dpadr': 45, 'kejki': 62}


def func2():
    return 'tfccj'


def func3():
    return 27.69


def func4():
    return (62, 69, 7)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
