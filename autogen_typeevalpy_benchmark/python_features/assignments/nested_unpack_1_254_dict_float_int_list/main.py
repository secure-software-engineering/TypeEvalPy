# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'lqjeu': 20, 'inhey': 36, 'bherg': 97}


def func2():
    return 43.48


def func3():
    return 96


def func4():
    return [72, 10, 98]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
