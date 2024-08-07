# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 54


def func2():
    return {'psxrv': 83, 'qyhrf': 46, 'lgjzj': 8}


def func3():
    return (51, 36, 25)


def func4():
    return 96.85


(a, b), (c, d) = [(func1, func2), (func3, func4)]
