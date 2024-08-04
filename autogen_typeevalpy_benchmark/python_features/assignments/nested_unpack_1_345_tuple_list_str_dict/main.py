# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (57, 50, 2)


def func2():
    return [51, 33, 39]


def func3():
    return 'cvgfx'


def func4():
    return {'xqwtk': 21, 'awvym': 90, 'kvswv': 34}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
