# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 29.63


def func2():
    return [24, 100, 37]


def func3():
    return {'xvmjw': 4, 'ntjtl': 60, 'fcvaj': 2}


def func4():
    return (21, 73, 100)


(a, b), (c, d) = [(func1, func2), (func3, func4)]