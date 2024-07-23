# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 90.75


def func2():
    return {'kliiw': 53, 'wiaqb': 86, 'mvbab': 18}


def func3():
    return [90, 31, 16]


def func4():
    return (33, 29, 63)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
