# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 53.86


def func2():
    return (94, 68, 87)


def func3():
    return {'pbtho': 28, 'dpjbl': 56, 'oqvoz': 5}


def func4():
    return 'xgauq'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
