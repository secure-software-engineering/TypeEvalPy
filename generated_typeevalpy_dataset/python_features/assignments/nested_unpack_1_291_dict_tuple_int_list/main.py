# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'lvvms': 65, 'slbbk': 43, 'xbaba': 60}


def func2():
    return (21, 92, 6)


def func3():
    return 29


def func4():
    return [37, 93, 29]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
