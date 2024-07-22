# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (22, 21, 86)


def func2():
    return [79, 32, 94]


def func3():
    return {'dzcuc': 9, 'fnskg': 78, 'yxzqq': 28}


def func4():
    return 'mkhca'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
