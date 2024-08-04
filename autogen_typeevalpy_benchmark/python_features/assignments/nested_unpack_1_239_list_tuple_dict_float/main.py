# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [70, 23, 76]


def func2():
    return (77, 59, 81)


def func3():
    return {'twlqn': 18, 'xmfci': 45, 'keant': 37}


def func4():
    return 47.45


(a, b), (c, d) = [(func1, func2), (func3, func4)]
