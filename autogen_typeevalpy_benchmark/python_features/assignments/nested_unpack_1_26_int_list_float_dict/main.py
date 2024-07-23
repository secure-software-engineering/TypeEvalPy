# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 81


def func2():
    return [41, 32, 31]


def func3():
    return 44.13


def func4():
    return {'zjsun': 75, 'ewamo': 99, 'xwijx': 17}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
