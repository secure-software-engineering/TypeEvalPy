# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'sblup'


def func2():
    return {'doxiz': 86, 'kdpby': 38, 'ghfio': 44}


def func3():
    return (52, 55, 78)


def func4():
    return 4.75


(a, b), (c, d) = [(func1, func2), (func3, func4)]
