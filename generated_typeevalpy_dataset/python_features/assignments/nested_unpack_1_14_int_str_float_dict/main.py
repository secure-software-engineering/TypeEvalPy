# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 27


def func2():
    return 'kqyjc'


def func3():
    return 4.59


def func4():
    return {'zmgrn': 74, 'bbfld': 9, 'lfdqw': 7}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
