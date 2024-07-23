# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'zvevo': 25, 'dytcd': 30, 'nbirf': 40}


def func2():
    return [29, 7, 76]


def func3():
    return (70, 83, 14)


def func4():
    return 'yplnr'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
