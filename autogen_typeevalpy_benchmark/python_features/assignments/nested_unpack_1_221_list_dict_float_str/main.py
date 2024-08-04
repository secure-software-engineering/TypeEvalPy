# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [70, 1, 100]


def func2():
    return {'rlkws': 33, 'lymtj': 62, 'uxvol': 99}


def func3():
    return 24.02


def func4():
    return 'whwke'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
