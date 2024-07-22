# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (4, 89, 32)


def func2():
    return 'npjto'


def func3():
    return {'rbfix': 49, 'rgnly': 99, 'xwrzx': 95}


def func4():
    return 68


(a, b), (c, d) = [(func1, func2), (func3, func4)]
