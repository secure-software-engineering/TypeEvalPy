# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'kpokm'


def func2():
    return 69


def func3():
    return (89, 83, 23)


def func4():
    return [72, 22, 63]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
