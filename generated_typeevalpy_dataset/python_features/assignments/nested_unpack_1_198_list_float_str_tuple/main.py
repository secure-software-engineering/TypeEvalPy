# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [29, 42, 62]


def func2():
    return 70.35


def func3():
    return 'eegga'


def func4():
    return (35, 37, 69)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
