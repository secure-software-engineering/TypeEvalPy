# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (84, 90, 10)


def func2():
    return {'kerlg': 76, 'mkega': 86, 'krona': 19}


def func3():
    return [37, 33, 21]


def func4():
    return 65.6


(a, b), (c, d) = [(func1, func2), (func3, func4)]
