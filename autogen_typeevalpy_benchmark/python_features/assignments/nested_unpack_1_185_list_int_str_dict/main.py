# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [6, 81, 69]


def func2():
    return 23


def func3():
    return 'nkybj'


def func4():
    return {'mdewn': 22, 'kkqtj': 1, 'qlvnt': 10}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
