# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'rlwzj': 39, 'blipf': 23, 'jmbgt': 38}


def func2():
    return (92, 2, 48)


def func3():
    return 65


def func4():
    return 15.16


(a, b), (c, d) = [(func1, func2), (func3, func4)]
