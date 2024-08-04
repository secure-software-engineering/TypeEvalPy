# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [67, 52, 77]


def func2():
    return {'zqwsv': 80, 'yfpmm': 85, 'fkdpt': 66}


def func3():
    return 34


def func4():
    return (22, 93, 88)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
