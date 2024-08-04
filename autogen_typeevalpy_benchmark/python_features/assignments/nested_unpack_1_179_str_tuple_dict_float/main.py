# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'izibl'


def func2():
    return (27, 98, 100)


def func3():
    return {'etmtc': 68, 'pqkzj': 25, 'afjai': 3}


def func4():
    return 68.0


(a, b), (c, d) = [(func1, func2), (func3, func4)]
