# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'delwx': 43, 'mvybn': 46, 'oroap': 9}


def func2():
    return 'zhazq'


def func3():
    return 84.4


def func4():
    return (74, 78, 50)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
