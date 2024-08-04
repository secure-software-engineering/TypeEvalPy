# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (21, 92, 69)


def func2():
    return 37


def func3():
    return [24, 23, 91]


def func4():
    return {'srdgb': 21, 'idgeo': 69, 'aiijo': 39}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
