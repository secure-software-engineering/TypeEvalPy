# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (92, 53, 1)


def func2():
    return {'iehqn': 82, 'mmusr': 81, 'efntp': 19}


def func3():
    return [48, 5, 39]


def func4():
    return 'hcsua'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
