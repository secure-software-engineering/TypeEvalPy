# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [67, 67, 89]


def func2():
    return 90


def func3():
    return {'qlsmr': 22, 'qdvxp': 10, 'aynmm': 97}


def func4():
    return (63, 42, 31)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
