# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [44, 59, 77]


def func2():
    return {'pfkcf': 16, 'wnkdc': 12, 'mpbun': 62}


def func3():
    return 66.28


def func4():
    return 78


(a, b), (c, d) = [(func1, func2), (func3, func4)]
