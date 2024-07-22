# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 15.02


def func2():
    return {'hhadq': 87, 'znrgp': 42, 'udgip': 71}


def func3():
    return (41, 63, 96)


def func4():
    return [14, 60, 84]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
