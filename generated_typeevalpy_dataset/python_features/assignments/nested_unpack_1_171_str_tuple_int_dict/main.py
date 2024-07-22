# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'jgocp'


def func2():
    return (80, 6, 43)


def func3():
    return 74


def func4():
    return {'ihmvh': 35, 'bptfj': 62, 'nmxcw': 87}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
