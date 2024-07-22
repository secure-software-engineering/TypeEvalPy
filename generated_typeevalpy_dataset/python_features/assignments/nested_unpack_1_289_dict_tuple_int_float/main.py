# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'xckej': 48, 'evsdj': 21, 'tddvj': 56}


def func2():
    return (5, 30, 31)


def func3():
    return 74


def func4():
    return 47.93


(a, b), (c, d) = [(func1, func2), (func3, func4)]
