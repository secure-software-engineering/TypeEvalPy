# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (15, 74, 95)


def func2():
    return [65, 16, 67]


def func3():
    return 66.76


def func4():
    return 'punmc'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
