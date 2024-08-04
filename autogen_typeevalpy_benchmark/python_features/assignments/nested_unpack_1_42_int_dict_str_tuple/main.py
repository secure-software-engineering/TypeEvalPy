# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 50


def func2():
    return {'wcjjh': 37, 'savka': 100, 'wuzxt': 30}


def func3():
    return 'pjqqr'


def func4():
    return (93, 99, 85)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
