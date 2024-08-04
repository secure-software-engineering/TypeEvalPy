# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 68.59


def func2():
    return {'roqje': 30, 'nnsfa': 32, 'ahron': 59}


def func3():
    return [45, 20, 36]


def func4():
    return 'ewtar'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
