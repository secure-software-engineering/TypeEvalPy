# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (85, 59, 78)


def func2():
    return 'jzmtr'


def func3():
    return {'uyxst': 64, 'qnzvz': 63, 'cjzcv': 61}


def func4():
    return [53, 22, 77]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
