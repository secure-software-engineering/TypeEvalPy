# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'drxoz': 99, 'xsgmy': 99, 'qxhlx': 42}


def func2():
    return [33, 21, 100]


def func3():
    return (10, 36, 100)


def func4():
    return 7.18


(a, b), (c, d) = [(func1, func2), (func3, func4)]
