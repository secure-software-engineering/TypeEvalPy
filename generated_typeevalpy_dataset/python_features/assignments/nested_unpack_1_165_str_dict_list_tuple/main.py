# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'onkbt'


def func2():
    return {'dxycz': 70, 'nwwxa': 61, 'prqsn': 68}


def func3():
    return [79, 12, 16]


def func4():
    return (75, 82, 45)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
