# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'jcipw': 4, 'pcnie': 39, 'ykmsu': 37}


def func2():
    return 73


def func3():
    return 'fcuhg'


def func4():
    return (88, 33, 95)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
