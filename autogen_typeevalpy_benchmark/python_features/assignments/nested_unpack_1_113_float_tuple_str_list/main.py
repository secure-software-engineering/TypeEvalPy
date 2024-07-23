# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 82.49


def func2():
    return (68, 91, 4)


def func3():
    return 'qjhwg'


def func4():
    return [61, 35, 9]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
