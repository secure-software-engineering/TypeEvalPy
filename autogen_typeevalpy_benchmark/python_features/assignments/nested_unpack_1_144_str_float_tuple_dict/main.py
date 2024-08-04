# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'kgqbx'


def func2():
    return 2.19


def func3():
    return (47, 41, 17)


def func4():
    return {'kvkoe': 92, 'mzbpa': 65, 'fxykh': 99}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
