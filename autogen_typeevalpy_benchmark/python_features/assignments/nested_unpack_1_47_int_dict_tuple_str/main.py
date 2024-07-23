# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 70


def func2():
    return {'xwvfi': 3, 'izwwk': 75, 'tsbbe': 26}


def func3():
    return (18, 11, 33)


def func4():
    return 'dkmhl'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
