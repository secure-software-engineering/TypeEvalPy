# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'cfkpd': 99, 'ulpko': 27, 'jxrae': 5}


def func2():
    return [45, 44, 13]


def func3():
    return 83


def func4():
    return 71.81


(a, b), (c, d) = [(func1, func2), (func3, func4)]
