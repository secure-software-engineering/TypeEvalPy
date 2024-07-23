# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 50.99


def func2():
    return {'gfgvh': 33, 'xztbe': 60, 'noitz': 58}


def func3():
    return 'trqhe'


def func4():
    return 44


(a, b), (c, d) = [(func1, func2), (func3, func4)]
