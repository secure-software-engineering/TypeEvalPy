# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [2, 89, 63]


def func2():
    return (97, 62, 39)


def func3():
    return {'alhga': 31, 'jkoke': 67, 'tkjgk': 98}


def func4():
    return 'upshq'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
