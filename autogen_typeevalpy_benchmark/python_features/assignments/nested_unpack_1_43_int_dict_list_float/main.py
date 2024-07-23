# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 54


def func2():
    return {'pcvnd': 62, 'rohck': 99, 'baiwu': 90}


def func3():
    return [7, 86, 38]


def func4():
    return 47.27


(a, b), (c, d) = [(func1, func2), (func3, func4)]
