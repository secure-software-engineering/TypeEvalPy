# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 9


def func2():
    return {'ncwpg': 17, 'hxcze': 50, 'qnyky': 78}


def func3():
    return 'uuyhl'


def func4():
    return [48, 89, 52]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
