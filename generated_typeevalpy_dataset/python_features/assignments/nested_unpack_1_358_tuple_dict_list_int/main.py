# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (95, 19, 76)


def func2():
    return {'uilpu': 94, 'oqdof': 19, 'fwepm': 1}


def func3():
    return [42, 7, 44]


def func4():
    return 93


(a, b), (c, d) = [(func1, func2), (func3, func4)]
