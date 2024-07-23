# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [47, 82, 51]


def func2():
    return (81, 20, 69)


def func3():
    return 20.96


def func4():
    return 'gxbxs'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
