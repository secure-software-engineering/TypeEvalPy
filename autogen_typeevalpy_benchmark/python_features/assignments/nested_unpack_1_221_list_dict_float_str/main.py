# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [51, 95, 51]


def func2():
    return {'ohmoj': 95, 'sfnti': 33, 'emmxl': 87}


def func3():
    return 67.1


def func4():
    return 'zdayi'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
