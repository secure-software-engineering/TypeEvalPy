# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'ozngg': 22, 'lrock': 45, 'jeiru': 79}


def func2():
    return 82.34


def func3():
    return 57


def func4():
    return [80, 19, 57]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
