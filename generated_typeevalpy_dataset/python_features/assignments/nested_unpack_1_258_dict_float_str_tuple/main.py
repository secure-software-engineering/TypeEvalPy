# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'kgips': 20, 'cksoo': 90, 'wloyw': 34}


def func2():
    return 44.4


def func3():
    return 'yxkpz'


def func4():
    return (99, 75, 15)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
