# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 55


def func2():
    return {'dhmuv': 6, 'rrlvd': 65, 'uihyv': 35}


def func3():
    return [99, 9, 61]


def func4():
    return (65, 16, 78)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
