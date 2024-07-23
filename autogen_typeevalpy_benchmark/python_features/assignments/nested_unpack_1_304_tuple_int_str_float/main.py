# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (77, 63, 55)


def func2():
    return 41


def func3():
    return 'dtluh'


def func4():
    return 83.95


(a, b), (c, d) = [(func1, func2), (func3, func4)]
