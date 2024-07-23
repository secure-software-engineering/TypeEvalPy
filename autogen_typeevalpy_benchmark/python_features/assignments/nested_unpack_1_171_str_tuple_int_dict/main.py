# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'ruujo'


def func2():
    return (60, 84, 8)


def func3():
    return 33


def func4():
    return {'ovnoy': 30, 'szzdx': 7, 'gezki': 96}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
