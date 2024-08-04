# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (4, 32, 40)


def func2():
    return [60, 63, 72]


def func3():
    return 56


def func4():
    return {'kxfha': 39, 'uhoqb': 9, 'subxi': 53}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
