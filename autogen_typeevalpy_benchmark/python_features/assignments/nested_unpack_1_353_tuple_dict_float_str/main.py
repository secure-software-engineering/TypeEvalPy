# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (56, 97, 19)


def func2():
    return {'tebwv': 36, 'oiucw': 84, 'rcaec': 55}


def func3():
    return 78.03


def func4():
    return 'fdcnr'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
