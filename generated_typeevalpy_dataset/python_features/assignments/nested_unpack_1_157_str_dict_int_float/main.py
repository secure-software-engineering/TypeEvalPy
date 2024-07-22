# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'ntyaz'


def func2():
    return {'teblh': 38, 'cwwut': 87, 'mkqiu': 76}


def func3():
    return 72


def func4():
    return 54.65


(a, b), (c, d) = [(func1, func2), (func3, func4)]
