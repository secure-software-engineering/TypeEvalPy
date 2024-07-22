# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'rycrb': 58, 'txahv': 81, 'jkwfv': 6}


def func2():
    return 13.64


def func3():
    return (83, 72, 85)


def func4():
    return [7, 46, 69]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
