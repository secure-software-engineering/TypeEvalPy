# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 74.38


def func2():
    return (3, 34, 71)


def func3():
    return 75


def func4():
    return {'pkdij': 46, 'vmrrg': 22, 'vzqme': 18}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
