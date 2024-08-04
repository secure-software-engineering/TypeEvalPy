# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'awwfp'


def func2():
    return 19.68


def func3():
    return (51, 38, 83)


def func4():
    return [7, 31, 64]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
