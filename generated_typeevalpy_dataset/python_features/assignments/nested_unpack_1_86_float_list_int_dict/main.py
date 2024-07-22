# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 13.41


def func2():
    return [46, 70, 98]


def func3():
    return 17


def func4():
    return {'cuywp': 38, 'efpcf': 27, 'tjind': 42}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
