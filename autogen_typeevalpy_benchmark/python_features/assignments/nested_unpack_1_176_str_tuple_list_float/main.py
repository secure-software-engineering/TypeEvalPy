# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'evcwm'


def func2():
    return (21, 82, 92)


def func3():
    return [12, 66, 18]


def func4():
    return 51.15


(a, b), (c, d) = [(func1, func2), (func3, func4)]
