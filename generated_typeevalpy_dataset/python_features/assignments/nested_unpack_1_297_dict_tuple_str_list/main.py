# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'bqzdu': 34, 'hstjv': 90, 'qieoq': 67}


def func2():
    return (75, 24, 18)


def func3():
    return 'ushhb'


def func4():
    return [4, 1, 32]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
