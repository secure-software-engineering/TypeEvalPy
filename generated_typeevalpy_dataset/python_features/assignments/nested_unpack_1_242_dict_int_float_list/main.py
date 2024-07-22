# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'yascy': 94, 'dqhsl': 91, 'ssarx': 89}


def func2():
    return 5


def func3():
    return 85.68


def func4():
    return [89, 14, 77]


(a, b), (c, d) = [(func1, func2), (func3, func4)]