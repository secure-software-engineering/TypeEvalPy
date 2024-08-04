# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 5


def func2():
    return {'dzicv': 51, 'cxadw': 84, 'zbugq': 11}


def func3():
    return 85.32


def func4():
    return (87, 69, 49)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
