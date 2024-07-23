# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'lfcxp'


def func2():
    return {'mvmwf': 90, 'lvqpz': 23, 'eojnn': 94}


def func3():
    return 69.42


def func4():
    return (16, 22, 41)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
