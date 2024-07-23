# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (84, 94, 97)


def func2():
    return {'ewbpz': 71, 'yzkox': 76, 'fbrxj': 77}


def func3():
    return 4


def func4():
    return 'eypmv'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
