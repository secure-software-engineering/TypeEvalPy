# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 10.96


def func2():
    return {'gxnrd': 83, 'ossec': 99, 'ivmwk': 56}


def func3():
    return 'blkpb'


def func4():
    return 80


(a, b), (c, d) = [(func1, func2), (func3, func4)]
