# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'hgrid'


def func2():
    return 31


def func3():
    return {'pfgau': 83, 'slnfn': 82, 'xwvzd': 33}


def func4():
    return (42, 73, 58)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
