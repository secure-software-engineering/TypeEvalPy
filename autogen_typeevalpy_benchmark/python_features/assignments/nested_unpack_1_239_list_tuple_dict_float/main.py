# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [89, 56, 26]


def func2():
    return (88, 37, 73)


def func3():
    return {'xnepo': 14, 'vrxik': 67, 'pebbd': 87}


def func4():
    return 19.05


(a, b), (c, d) = [(func1, func2), (func3, func4)]
