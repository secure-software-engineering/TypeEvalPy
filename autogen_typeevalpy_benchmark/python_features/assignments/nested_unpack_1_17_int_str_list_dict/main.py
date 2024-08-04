# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 97


def func2():
    return 'gqtnq'


def func3():
    return [36, 57, 10]


def func4():
    return {'sgixc': 99, 'djdfk': 75, 'imbvk': 90}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
