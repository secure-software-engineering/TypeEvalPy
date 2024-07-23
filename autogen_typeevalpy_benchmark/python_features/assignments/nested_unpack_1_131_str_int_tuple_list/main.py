# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'rhljp'


def func2():
    return 93


def func3():
    return (80, 82, 70)


def func4():
    return [28, 48, 29]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
