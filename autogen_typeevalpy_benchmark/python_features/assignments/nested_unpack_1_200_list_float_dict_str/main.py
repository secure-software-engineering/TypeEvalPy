# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [17, 91, 76]


def func2():
    return 16.96


def func3():
    return {'jkasr': 49, 'gsfhx': 24, 'savie': 59}


def func4():
    return 'ihbcg'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
