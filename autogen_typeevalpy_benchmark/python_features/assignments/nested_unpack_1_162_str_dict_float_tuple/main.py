# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'tgzex'


def func2():
    return {'csqxl': 64, 'ggbgc': 49, 'aktzw': 45}


def func3():
    return 55.06


def func4():
    return (13, 62, 74)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
