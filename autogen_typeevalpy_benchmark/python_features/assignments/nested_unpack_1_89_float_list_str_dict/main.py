# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 3.81


def func2():
    return [46, 55, 93]


def func3():
    return 'cfses'


def func4():
    return {'hfywb': 54, 'oyxnu': 82, 'lcvcd': 72}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
