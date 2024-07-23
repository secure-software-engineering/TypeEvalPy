# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'vyhwe': 94, 'mwflz': 85, 'egwmj': 3}


def func2():
    return 21


def func3():
    return [27, 22, 43]


def func4():
    return (12, 54, 9)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
