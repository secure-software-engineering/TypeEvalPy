# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'kojzo': 11, 'scmrd': 67, 'tzzum': 79}


def func2():
    return [12, 32, 61]


def func3():
    return 63.44


def func4():
    return 'rrrop'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
