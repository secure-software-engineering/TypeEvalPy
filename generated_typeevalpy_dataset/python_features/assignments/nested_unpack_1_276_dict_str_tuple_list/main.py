# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'cuuuc': 28, 'wiuxa': 82, 'lcezi': 84}


def func2():
    return 'cxozs'


def func3():
    return (12, 22, 2)


def func4():
    return [61, 60, 67]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
