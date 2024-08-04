# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'cpgoq': 12, 'ovbdq': 7, 'awrvh': 14}


def func2():
    return 'kerpr'


def func3():
    return 77


def func4():
    return [74, 72, 23]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
