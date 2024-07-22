# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'mpaax': 60, 'ffpik': 79, 'jouyb': 59}


def func2():
    return 'defwt'


def func3():
    return 67.79


def func4():
    return [73, 83, 84]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
