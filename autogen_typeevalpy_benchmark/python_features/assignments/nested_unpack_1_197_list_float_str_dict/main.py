# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [75, 23, 94]


def func2():
    return 81.71


def func3():
    return 'crpiw'


def func4():
    return {'kpsgk': 95, 'ihudp': 71, 'xnvoi': 81}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
