# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'pnxxp'


def func2():
    return 85.0


def func3():
    return [54, 86, 100]


def func4():
    return {'fmvjl': 64, 'ywxko': 71, 'lkrwf': 81}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
