# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 13


def func2():
    return (71, 53, 93)


def func3():
    return {'kcfds': 56, 'xdffh': 65, 'jfmgz': 70}


def func4():
    return 66.41


(a, b), (c, d) = [(func1, func2), (func3, func4)]
