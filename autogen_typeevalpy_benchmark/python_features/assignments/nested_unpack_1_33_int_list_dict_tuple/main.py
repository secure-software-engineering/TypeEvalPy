# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 81


def func2():
    return [26, 48, 97]


def func3():
    return {'qbtmd': 53, 'omkai': 83, 'wsxvc': 53}


def func4():
    return (47, 57, 53)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
