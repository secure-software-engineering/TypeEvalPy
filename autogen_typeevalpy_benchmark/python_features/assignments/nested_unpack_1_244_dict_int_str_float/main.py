# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'glaup': 88, 'kgzpr': 80, 'reugm': 44}


def func2():
    return 98


def func3():
    return 'qbqsu'


def func4():
    return 13.46


(a, b), (c, d) = [(func1, func2), (func3, func4)]
