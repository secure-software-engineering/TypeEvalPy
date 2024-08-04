# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (35, 73, 77)


def func2():
    return {'ktvpl': 38, 'lbimf': 60, 'remqn': 56}


def func3():
    return 'cuhzr'


def func4():
    return 30.74


(a, b), (c, d) = [(func1, func2), (func3, func4)]
