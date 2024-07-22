# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'eqfyw'


def func2():
    return {'rbhob': 22, 'gerly': 81, 'kuhlp': 53}


def func3():
    return [77, 34, 62]


def func4():
    return 85


(a, b), (c, d) = [(func1, func2), (func3, func4)]
