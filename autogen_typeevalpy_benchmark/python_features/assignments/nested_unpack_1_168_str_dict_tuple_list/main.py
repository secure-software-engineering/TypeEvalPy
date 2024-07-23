# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'vlcge'


def func2():
    return {'xkdsm': 7, 'dxfwy': 18, 'yeiqa': 95}


def func3():
    return (82, 26, 91)


def func4():
    return [79, 66, 18]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
