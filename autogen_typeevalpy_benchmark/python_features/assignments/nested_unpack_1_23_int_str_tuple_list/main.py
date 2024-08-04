# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 59


def func2():
    return 'sltzh'


def func3():
    return (69, 100, 62)


def func4():
    return [60, 56, 94]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
