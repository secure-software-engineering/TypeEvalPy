# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'xveqr': 26, 'wlglj': 70, 'vnjme': 83}


def func2():
    return 'kfhgw'


def func3():
    return [49, 78, 54]


def func4():
    return (79, 53, 4)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
