# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (78, 81, 17)


def func2():
    return 77.42


def func3():
    return [91, 76, 23]


def func4():
    return 45


(a, b), (c, d) = [(func1, func2), (func3, func4)]
