# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'cjhjv'


def func2():
    return 87.58


def func3():
    return {'qrbop': 16, 'ejftx': 76, 'qlfxd': 94}


def func4():
    return (50, 45, 55)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
