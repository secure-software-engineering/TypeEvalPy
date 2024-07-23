# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'ybhov': 19, 'lbzgy': 55, 'fulal': 93}


def func2():
    return 86


def func3():
    return 'upaoe'


def func4():
    return (58, 4, 28)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
