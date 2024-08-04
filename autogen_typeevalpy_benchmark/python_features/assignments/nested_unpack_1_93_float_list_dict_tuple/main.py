# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 62.35


def func2():
    return [49, 19, 88]


def func3():
    return {'gosel': 72, 'kkfnp': 42, 'mwssn': 85}


def func4():
    return (62, 68, 49)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
