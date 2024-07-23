# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [85, 40, 79]


def func2():
    return {'wvzsu': 40, 'ulxmu': 44, 'ghquk': 70}


def func3():
    return 'jytct'


def func4():
    return (56, 22, 53)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
