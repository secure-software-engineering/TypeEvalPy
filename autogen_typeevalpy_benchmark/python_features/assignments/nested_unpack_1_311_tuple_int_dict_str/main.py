# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (30, 73, 96)


def func2():
    return 93


def func3():
    return {'yfify': 61, 'npdrg': 13, 'adxoa': 51}


def func4():
    return 'fidzc'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
