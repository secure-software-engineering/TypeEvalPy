# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [75, 70, 73]


def func2():
    return {'eqjqv': 18, 'njxnj': 57, 'wmmpn': 22}


def func3():
    return 30


def func4():
    return 8.63


(a, b), (c, d) = [(func1, func2), (func3, func4)]
