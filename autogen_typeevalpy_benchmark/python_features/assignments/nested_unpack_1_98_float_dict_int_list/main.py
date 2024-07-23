# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 16.22


def func2():
    return {'lrwif': 37, 'gtzjh': 56, 'ypzsa': 36}


def func3():
    return 52


def func4():
    return [11, 7, 92]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
