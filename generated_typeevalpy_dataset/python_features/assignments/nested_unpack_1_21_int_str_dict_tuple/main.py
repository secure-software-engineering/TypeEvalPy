# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 66


def func2():
    return 'gspjm'


def func3():
    return {'xtfok': 15, 'csupl': 34, 'apswy': 46}


def func4():
    return (68, 56, 32)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
