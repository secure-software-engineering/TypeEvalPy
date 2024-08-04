# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (52, 33, 23)


def func2():
    return {'gukaf': 78, 'kkqye': 17, 'hutxx': 46}


def func3():
    return 'rvnmx'


def func4():
    return 61


(a, b), (c, d) = [(func1, func2), (func3, func4)]
