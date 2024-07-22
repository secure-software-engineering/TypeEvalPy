# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 88.89


def func2():
    return 'rgoee'


def func3():
    return (99, 88, 19)


def func4():
    return [2, 18, 51]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
