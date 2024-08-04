# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 26


def func2():
    return [55, 15, 70]


def func3():
    return {'fdgdb': 57, 'upvxl': 11, 'mhkho': 77}


def func4():
    return 'bligc'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
