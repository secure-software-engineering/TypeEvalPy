# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'dwrjq': 58, 'quynq': 81, 'wzfvq': 50}


def func2():
    return [25, 76, 30]


def func3():
    return 93.85


def func4():
    return 82


(a, b), (c, d) = [(func1, func2), (func3, func4)]
