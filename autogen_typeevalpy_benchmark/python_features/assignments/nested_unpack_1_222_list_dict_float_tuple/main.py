# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [68, 35, 16]


def func2():
    return {'iiuqo': 73, 'yvght': 14, 'tdzys': 55}


def func3():
    return 15.1


def func4():
    return (25, 28, 2)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
