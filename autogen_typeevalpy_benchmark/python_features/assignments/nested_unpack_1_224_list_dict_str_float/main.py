# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [61, 77, 56]


def func2():
    return {'cgjps': 85, 'ykrhz': 67, 'buema': 37}


def func3():
    return 'funsp'


def func4():
    return 67.73


(a, b), (c, d) = [(func1, func2), (func3, func4)]
