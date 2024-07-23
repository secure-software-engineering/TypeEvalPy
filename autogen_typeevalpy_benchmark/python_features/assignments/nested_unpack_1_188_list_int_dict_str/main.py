# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [80, 80, 33]


def func2():
    return 22


def func3():
    return {'xnvqh': 97, 'jvpkh': 55, 'txxuf': 38}


def func4():
    return 'pxayb'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
