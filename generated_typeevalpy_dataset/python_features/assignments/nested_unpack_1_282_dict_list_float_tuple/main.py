# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'fbgvs': 57, 'zsfbf': 6, 'omdnu': 46}


def func2():
    return [78, 86, 73]


def func3():
    return 2.93


def func4():
    return (67, 92, 57)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
