# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (76, 28, 8)


def func2():
    return 89


def func3():
    return [38, 78, 62]


def func4():
    return 'rtash'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
