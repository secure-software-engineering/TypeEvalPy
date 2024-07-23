# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 57


def func2():
    return 'mntia'


def func3():
    return {'dakle': 18, 'tgswi': 32, 'xndak': 82}


def func4():
    return (95, 86, 33)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
