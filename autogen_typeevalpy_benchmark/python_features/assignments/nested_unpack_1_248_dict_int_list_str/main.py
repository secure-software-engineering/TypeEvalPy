# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'xwqur': 27, 'onilh': 35, 'wowok': 10}


def func2():
    return 96


def func3():
    return [25, 95, 65]


def func4():
    return 'xkqaq'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
