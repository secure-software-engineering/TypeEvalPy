# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [9, 4, 29]


def func2():
    return 'xijra'


def func3():
    return (49, 29, 45)


def func4():
    return {'jildl': 56, 'hclah': 14, 'fzkcp': 58}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
