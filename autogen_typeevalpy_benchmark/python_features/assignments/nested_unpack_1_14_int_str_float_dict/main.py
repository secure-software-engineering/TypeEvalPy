# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 7


def func2():
    return 'czbsw'


def func3():
    return 26.32


def func4():
    return {'iafjx': 76, 'vtkqp': 60, 'flocp': 86}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
