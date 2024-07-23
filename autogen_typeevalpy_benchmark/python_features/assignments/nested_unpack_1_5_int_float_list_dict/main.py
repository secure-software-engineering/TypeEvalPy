# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 1


def func2():
    return 96.67


def func3():
    return [8, 76, 52]


def func4():
    return {'axdcj': 22, 'svggx': 12, 'pmzhm': 7}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
