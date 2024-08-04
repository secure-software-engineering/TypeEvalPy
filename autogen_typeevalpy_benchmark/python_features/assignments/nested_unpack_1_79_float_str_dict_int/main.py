# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 28.18


def func2():
    return 'zybqj'


def func3():
    return {'urydp': 48, 'uabuj': 57, 'jopry': 98}


def func4():
    return 10


(a, b), (c, d) = [(func1, func2), (func3, func4)]
