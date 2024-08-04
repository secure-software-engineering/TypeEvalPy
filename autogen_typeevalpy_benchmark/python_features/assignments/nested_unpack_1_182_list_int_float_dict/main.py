# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [99, 69, 80]


def func2():
    return 7


def func3():
    return 59.8


def func4():
    return {'bcvbd': 80, 'ldgsf': 78, 'rakcn': 90}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
