# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'dgpal'


def func2():
    return 86


def func3():
    return [98, 24, 33]


def func4():
    return (51, 79, 87)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
