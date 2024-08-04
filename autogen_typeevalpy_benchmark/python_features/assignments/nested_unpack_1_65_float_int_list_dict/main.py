# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 39.27


def func2():
    return 33


def func3():
    return [93, 85, 78]


def func4():
    return {'wipdj': 95, 'zskpy': 88, 'ijuvr': 68}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
