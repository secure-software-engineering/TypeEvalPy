# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 27


def func2():
    return [81, 28, 34]


def func3():
    return {'reeba': 81, 'lphgs': 76, 'slryu': 85}


def func4():
    return 80.59


(a, b), (c, d) = [(func1, func2), (func3, func4)]
