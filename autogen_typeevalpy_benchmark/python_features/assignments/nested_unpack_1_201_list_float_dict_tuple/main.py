# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [2, 96, 33]


def func2():
    return 21.11


def func3():
    return {'wwlfq': 23, 'sjptf': 95, 'sflzb': 66}


def func4():
    return (16, 49, 6)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
