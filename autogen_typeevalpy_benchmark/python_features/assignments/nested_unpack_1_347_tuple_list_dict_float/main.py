# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (30, 35, 91)


def func2():
    return [52, 85, 35]


def func3():
    return {'ntpxz': 10, 'utwps': 91, 'cpoqp': 57}


def func4():
    return 30.31


(a, b), (c, d) = [(func1, func2), (func3, func4)]
