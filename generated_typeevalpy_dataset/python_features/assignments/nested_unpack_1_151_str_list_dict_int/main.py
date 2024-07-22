# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'kgjgj'


def func2():
    return [74, 18, 36]


def func3():
    return {'fnivi': 87, 'wfebi': 96, 'onaly': 84}


def func4():
    return 48


(a, b), (c, d) = [(func1, func2), (func3, func4)]
