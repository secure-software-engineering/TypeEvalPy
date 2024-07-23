# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'fdzbw': 7, 'mhbfa': 54, 'tzath': 58}


def func2():
    return (85, 25, 27)


def func3():
    return [87, 18, 37]


def func4():
    return 'qqoqr'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
