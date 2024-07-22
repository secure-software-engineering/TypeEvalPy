# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'oshzm'


def func2():
    return 87


def func3():
    return {'vpwhs': 34, 'xlnxf': 12, 'ozlmk': 10}


def func4():
    return [13, 50, 88]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
