# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'ojqbt': 50, 'dzjro': 41, 'ialen': 36}


def func2():
    return 30


def func3():
    return 60.48


def func4():
    return 'rqxac'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
