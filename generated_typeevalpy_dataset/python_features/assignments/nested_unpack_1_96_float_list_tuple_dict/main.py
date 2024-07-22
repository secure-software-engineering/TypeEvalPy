# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 89.7


def func2():
    return [39, 23, 88]


def func3():
    return (77, 28, 35)


def func4():
    return {'pmdkt': 7, 'bphvm': 14, 'ibehv': 52}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
