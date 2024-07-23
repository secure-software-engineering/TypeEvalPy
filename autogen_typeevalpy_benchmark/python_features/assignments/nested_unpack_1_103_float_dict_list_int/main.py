# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 48.63


def func2():
    return {'uzlpt': 9, 'eutlc': 20, 'qhuhb': 31}


def func3():
    return [26, 40, 84]


def func4():
    return 20


(a, b), (c, d) = [(func1, func2), (func3, func4)]
