# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'cyixy'


def func2():
    return [17, 7, 61]


def func3():
    return {'wnqus': 61, 'hlgxm': 15, 'ahxfr': 51}


def func4():
    return 34.9


(a, b), (c, d) = [(func1, func2), (func3, func4)]
