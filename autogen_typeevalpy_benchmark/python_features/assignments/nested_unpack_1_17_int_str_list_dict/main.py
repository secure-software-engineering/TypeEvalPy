# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 61


def func2():
    return 'hsdjc'


def func3():
    return [31, 1, 9]


def func4():
    return {'hpbhr': 45, 'phley': 73, 'gjdvc': 82}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
