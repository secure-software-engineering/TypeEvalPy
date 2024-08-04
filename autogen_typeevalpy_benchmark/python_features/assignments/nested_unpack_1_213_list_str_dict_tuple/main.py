# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [56, 36, 47]


def func2():
    return 'dtwmj'


def func3():
    return {'hoepv': 75, 'wdogx': 75, 'bbana': 52}


def func4():
    return (99, 76, 28)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
