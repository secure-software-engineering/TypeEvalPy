# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (26, 71, 1)


def func2():
    return 74.84


def func3():
    return 'zyuhb'


def func4():
    return [41, 79, 12]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
