# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [42, 87, 66]


def func2():
    return (63, 100, 95)


def func3():
    return 'lcpmy'


def func4():
    return 22


(a, b), (c, d) = [(func1, func2), (func3, func4)]
