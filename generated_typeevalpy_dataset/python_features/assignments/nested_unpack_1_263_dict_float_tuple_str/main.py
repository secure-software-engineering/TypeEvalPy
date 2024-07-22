# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'jyzcu': 99, 'heujc': 39, 'yylfl': 85}


def func2():
    return 80.42


def func3():
    return (29, 31, 33)


def func4():
    return 'qbpsf'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
