# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 23.79


def func2():
    return {'kgwvg': 22, 'htufc': 88, 'csjlu': 33}


def func3():
    return 'cuwtw'


def func4():
    return [24, 2, 14]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
