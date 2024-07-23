# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (93, 72, 16)


def func2():
    return {'sdhkx': 7, 'tooet': 60, 'wobaz': 12}


def func3():
    return 'lofvy'


def func4():
    return 66


(a, b), (c, d) = [(func1, func2), (func3, func4)]
