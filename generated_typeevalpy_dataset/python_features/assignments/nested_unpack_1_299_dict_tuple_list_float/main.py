# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'ltkxs': 34, 'gfmga': 75, 'zpdpt': 92}


def func2():
    return (39, 48, 26)


def func3():
    return [44, 58, 2]


def func4():
    return 52.66


(a, b), (c, d) = [(func1, func2), (func3, func4)]
