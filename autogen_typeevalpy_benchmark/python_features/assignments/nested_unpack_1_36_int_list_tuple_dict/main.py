# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 67


def func2():
    return [47, 80, 97]


def func3():
    return (64, 81, 57)


def func4():
    return {'tfoyl': 15, 'sdzpg': 60, 'eoocz': 16}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
