# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'xpjix'


def func2():
    return 48


def func3():
    return {'ygpea': 2, 'zareb': 58, 'veykv': 42}


def func4():
    return (22, 71, 90)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
