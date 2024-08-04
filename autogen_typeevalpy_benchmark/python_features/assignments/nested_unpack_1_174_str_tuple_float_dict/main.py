# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'pyssh'


def func2():
    return (49, 45, 59)


def func3():
    return 25.95


def func4():
    return {'mrvkc': 82, 'nrvjq': 42, 'phcbz': 36}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
