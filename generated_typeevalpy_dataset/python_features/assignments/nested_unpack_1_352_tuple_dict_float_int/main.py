# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (16, 59, 74)


def func2():
    return {'sshlb': 92, 'brrpc': 48, 'yykse': 76}


def func3():
    return 4.25


def func4():
    return 67


(a, b), (c, d) = [(func1, func2), (func3, func4)]
