# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (35, 40, 12)


def func2():
    return 'rpmsa'


def func3():
    return {'grlkv': 66, 'ndjgb': 98, 'cxtkl': 68}


def func4():
    return [63, 99, 81]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
