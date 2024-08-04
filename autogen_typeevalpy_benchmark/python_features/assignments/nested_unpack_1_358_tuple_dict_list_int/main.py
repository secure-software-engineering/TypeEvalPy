# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (80, 34, 44)


def func2():
    return {'zweet': 96, 'pwcna': 78, 'demrw': 93}


def func3():
    return [63, 39, 80]


def func4():
    return 79


(a, b), (c, d) = [(func1, func2), (func3, func4)]
