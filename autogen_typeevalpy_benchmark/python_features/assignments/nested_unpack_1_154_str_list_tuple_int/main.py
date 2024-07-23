# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'wajad'


def func2():
    return [84, 79, 31]


def func3():
    return (76, 22, 17)


def func4():
    return 65


(a, b), (c, d) = [(func1, func2), (func3, func4)]
