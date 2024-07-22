# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 8.62


def func2():
    return [27, 85, 8]


def func3():
    return 'aidbs'


def func4():
    return {'fizyg': 95, 'mwmqp': 38, 'alzto': 51}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
