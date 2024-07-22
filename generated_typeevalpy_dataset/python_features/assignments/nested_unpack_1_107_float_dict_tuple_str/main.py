# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 65.67


def func2():
    return {'knilj': 80, 'nndhy': 80, 'mkqha': 41}


def func3():
    return (19, 99, 76)


def func4():
    return 'urbfc'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
