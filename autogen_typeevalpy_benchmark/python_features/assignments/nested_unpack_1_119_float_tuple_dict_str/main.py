# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 18.51


def func2():
    return (64, 65, 13)


def func3():
    return {'pcxny': 78, 'alria': 60, 'cftsg': 44}


def func4():
    return 'rnuvt'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
