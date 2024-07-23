# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 70


def func2():
    return [5, 30, 69]


def func3():
    return 'eozfd'


def func4():
    return (78, 35, 94)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
