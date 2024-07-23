# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 51.31


def func2():
    return 'zaptx'


def func3():
    return {'yekab': 2, 'ndvkx': 60, 'kvdnu': 3}


def func4():
    return (69, 5, 93)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
