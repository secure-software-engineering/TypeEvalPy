# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [17, 7, 68]


def func2():
    return (55, 62, 70)


def func3():
    return 5


def func4():
    return 50.75


(a, b), (c, d) = [(func1, func2), (func3, func4)]
