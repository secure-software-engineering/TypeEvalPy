# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (64, 15, 88)


def func2():
    return [55, 92, 25]


def func3():
    return 38.18


def func4():
    return {'kmrmh': 70, 'drohq': 68, 'svncf': 88}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
