# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'qwmhv': 45, 'idone': 26, 'hkybp': 77}


def func2():
    return 14


def func3():
    return 80.9


def func4():
    return (68, 15, 11)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
