# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 94


def func2():
    return {'hxnad': 32, 'tvvar': 76, 'njinw': 19}


def func3():
    return [97, 1, 36]


def func4():
    return (15, 9, 61)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
