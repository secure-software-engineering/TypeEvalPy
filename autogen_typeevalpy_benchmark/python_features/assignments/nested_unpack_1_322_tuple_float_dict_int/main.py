# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (48, 84, 8)


def func2():
    return 95.17


def func3():
    return {'ohnji': 52, 'vlqaq': 87, 'poifr': 38}


def func4():
    return 16


(a, b), (c, d) = [(func1, func2), (func3, func4)]
