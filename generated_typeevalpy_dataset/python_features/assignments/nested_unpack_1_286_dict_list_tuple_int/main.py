# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'ubpvb': 96, 'kiwlz': 57, 'hxgdy': 20}


def func2():
    return [50, 68, 12]


def func3():
    return (43, 10, 10)


def func4():
    return 83


(a, b), (c, d) = [(func1, func2), (func3, func4)]
