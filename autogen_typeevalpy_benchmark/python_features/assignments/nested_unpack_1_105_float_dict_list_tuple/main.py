# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 61.88


def func2():
    return {'yxgbp': 38, 'lrwgb': 30, 'lotud': 94}


def func3():
    return [74, 41, 74]


def func4():
    return (77, 99, 87)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
