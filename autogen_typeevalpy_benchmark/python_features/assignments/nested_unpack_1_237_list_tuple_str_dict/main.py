# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [91, 35, 78]


def func2():
    return (83, 51, 35)


def func3():
    return 'xuytn'


def func4():
    return {'lewdg': 68, 'gttfk': 98, 'cymbu': 11}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
