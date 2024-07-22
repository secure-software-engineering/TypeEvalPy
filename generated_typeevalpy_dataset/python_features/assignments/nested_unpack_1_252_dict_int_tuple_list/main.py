# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'eplvq': 31, 'kzcnx': 47, 'jpudo': 79}


def func2():
    return 3


def func3():
    return (23, 37, 3)


def func4():
    return [98, 76, 57]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
