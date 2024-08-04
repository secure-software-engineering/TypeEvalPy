# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 42


def func2():
    return 40.84


def func3():
    return (38, 71, 17)


def func4():
    return {'erjte': 66, 'okvhf': 61, 'upilr': 95}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
