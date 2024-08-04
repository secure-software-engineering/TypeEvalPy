# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 17.08


def func2():
    return (31, 73, 50)


def func3():
    return {'rojtu': 100, 'rctic': 42, 'gbppp': 4}


def func4():
    return 82


(a, b), (c, d) = [(func1, func2), (func3, func4)]
