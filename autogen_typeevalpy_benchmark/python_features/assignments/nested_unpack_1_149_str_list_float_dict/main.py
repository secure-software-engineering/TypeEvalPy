# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'xsntp'


def func2():
    return [94, 95, 21]


def func3():
    return 26.62


def func4():
    return {'mapki': 31, 'jqiaj': 38, 'yzxcl': 4}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
