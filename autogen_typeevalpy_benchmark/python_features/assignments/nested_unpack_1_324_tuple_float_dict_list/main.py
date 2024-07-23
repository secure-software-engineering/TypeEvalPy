# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (89, 3, 91)


def func2():
    return 44.63


def func3():
    return {'vmhes': 63, 'rxbyi': 25, 'lmjia': 94}


def func4():
    return [56, 42, 18]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
