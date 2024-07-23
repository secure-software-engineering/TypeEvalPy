# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (70, 48, 93)


def func2():
    return [12, 15, 26]


def func3():
    return {'rnixm': 28, 'pfsfz': 3, 'hmvbi': 19}


def func4():
    return 99


(a, b), (c, d) = [(func1, func2), (func3, func4)]
