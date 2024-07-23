# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [30, 67, 12]


def func2():
    return {'pwbyy': 99, 'usfuw': 26, 'cofzn': 64}


def func3():
    return 30


def func4():
    return 69.15


(a, b), (c, d) = [(func1, func2), (func3, func4)]
