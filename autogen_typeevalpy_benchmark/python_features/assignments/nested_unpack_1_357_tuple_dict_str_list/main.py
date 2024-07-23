# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (73, 68, 72)


def func2():
    return {'wmcua': 82, 'eplph': 63, 'lemmd': 15}


def func3():
    return 'qqgnp'


def func4():
    return [71, 82, 24]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
