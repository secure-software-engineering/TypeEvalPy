# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'zelwu': 24, 'hehxr': 100, 'xmqcn': 75}


def func2():
    return 93.85


def func3():
    return (90, 70, 18)


def func4():
    return 'kialx'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
