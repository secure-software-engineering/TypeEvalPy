# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'fesss'


def func2():
    return {'ghgbo': 38, 'vdjlh': 11, 'rpfae': 61}


def func3():
    return [15, 40, 51]


def func4():
    return 47.62


(a, b), (c, d) = [(func1, func2), (func3, func4)]
