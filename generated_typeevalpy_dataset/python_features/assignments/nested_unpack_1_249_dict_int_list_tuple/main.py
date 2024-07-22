# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'osawv': 93, 'cswsi': 20, 'epmqj': 74}


def func2():
    return 52


def func3():
    return [94, 81, 65]


def func4():
    return (47, 13, 16)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
