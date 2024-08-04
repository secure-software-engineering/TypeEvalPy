# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'zkioq': 93, 'afhui': 73, 'niari': 79}


def func2():
    return 'yvfvx'


def func3():
    return 48.43


def func4():
    return [61, 5, 83]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
