# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'brbex': 71, 'ghxgf': 93, 'fztww': 16}


def func2():
    return [81, 49, 19]


def func3():
    return 'cglie'


def func4():
    return 76.52


(a, b), (c, d) = [(func1, func2), (func3, func4)]
