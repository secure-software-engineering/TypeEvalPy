# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 40


def func2():
    return (46, 14, 74)


def func3():
    return 'nemwj'


def func4():
    return {'ochfl': 98, 'otqro': 40, 'prsah': 44}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
