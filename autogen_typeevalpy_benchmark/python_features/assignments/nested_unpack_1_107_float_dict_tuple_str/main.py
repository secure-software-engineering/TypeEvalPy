# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 55.28


def func2():
    return {'cdcgz': 34, 'floiu': 21, 'ibaln': 64}


def func3():
    return (98, 50, 42)


def func4():
    return 'nxfmx'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
