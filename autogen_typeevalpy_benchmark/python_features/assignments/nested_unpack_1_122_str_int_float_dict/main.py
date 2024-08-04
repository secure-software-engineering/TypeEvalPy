# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'mqlda'


def func2():
    return 51


def func3():
    return 33.89


def func4():
    return {'quiiv': 89, 'wzdiy': 82, 'fizzh': 63}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
