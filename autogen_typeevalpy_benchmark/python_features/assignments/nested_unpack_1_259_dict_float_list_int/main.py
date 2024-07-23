# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'jifpb': 20, 'jwgsi': 89, 'llaah': 26}


def func2():
    return 85.46


def func3():
    return [53, 70, 34]


def func4():
    return 77


(a, b), (c, d) = [(func1, func2), (func3, func4)]
