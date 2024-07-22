# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [77, 27, 33]


def func2():
    return (91, 81, 37)


def func3():
    return 'oksyp'


def func4():
    return 35


(a, b), (c, d) = [(func1, func2), (func3, func4)]
