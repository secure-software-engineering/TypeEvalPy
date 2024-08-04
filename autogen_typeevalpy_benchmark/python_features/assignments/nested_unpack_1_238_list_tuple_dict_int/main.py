# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [14, 34, 80]


def func2():
    return (20, 11, 84)


def func3():
    return {'ykftl': 71, 'dneaj': 57, 'xwmwy': 18}


def func4():
    return 90


(a, b), (c, d) = [(func1, func2), (func3, func4)]
