# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (40, 9, 45)


def func2():
    return [22, 95, 96]


def func3():
    return {'glagr': 62, 'ffqok': 60, 'nplzz': 47}


def func4():
    return 'auyft'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
