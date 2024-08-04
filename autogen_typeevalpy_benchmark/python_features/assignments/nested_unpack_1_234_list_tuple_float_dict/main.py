# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [13, 89, 21]


def func2():
    return (8, 28, 33)


def func3():
    return 48.18


def func4():
    return {'qlijo': 100, 'ygadw': 37, 'zfoqe': 46}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
