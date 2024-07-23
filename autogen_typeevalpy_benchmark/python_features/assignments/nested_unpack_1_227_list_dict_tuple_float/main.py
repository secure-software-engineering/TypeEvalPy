# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [74, 24, 71]


def func2():
    return {'hikaq': 55, 'umzqr': 82, 'krdtq': 50}


def func3():
    return (3, 79, 83)


def func4():
    return 87.21


(a, b), (c, d) = [(func1, func2), (func3, func4)]
