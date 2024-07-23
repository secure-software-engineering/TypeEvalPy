# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'qldow': 39, 'nmsxr': 42, 'bfnzd': 28}


def func2():
    return (94, 82, 11)


def func3():
    return 65.32


def func4():
    return 82


(a, b), (c, d) = [(func1, func2), (func3, func4)]
