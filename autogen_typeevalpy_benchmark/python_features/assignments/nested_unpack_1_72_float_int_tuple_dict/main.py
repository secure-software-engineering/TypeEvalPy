# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 70.85


def func2():
    return 58


def func3():
    return (79, 1, 11)


def func4():
    return {'afdyp': 69, 'lugdg': 3, 'qqbvm': 81}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
