# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'iqogx': 54, 'kdjgz': 21, 'hvsog': 21}


def func2():
    return (39, 14, 54)


def func3():
    return 79.3


def func4():
    return [83, 20, 81]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
