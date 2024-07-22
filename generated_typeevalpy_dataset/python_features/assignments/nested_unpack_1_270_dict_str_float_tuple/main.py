# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'uapvv': 45, 'ysjsn': 54, 'ssotg': 15}


def func2():
    return 'mtdcd'


def func3():
    return 71.02


def func4():
    return (13, 12, 18)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
