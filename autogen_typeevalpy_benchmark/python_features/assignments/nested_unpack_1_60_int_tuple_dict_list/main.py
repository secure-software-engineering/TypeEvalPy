# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 26


def func2():
    return (39, 11, 7)


def func3():
    return {'pxemw': 27, 'zvjen': 57, 'rxkjd': 65}


def func4():
    return [65, 52, 97]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
