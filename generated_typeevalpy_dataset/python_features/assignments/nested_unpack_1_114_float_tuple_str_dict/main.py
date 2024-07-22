# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 77.94


def func2():
    return (21, 94, 11)


def func3():
    return 'qieqy'


def func4():
    return {'ixoqz': 27, 'khtyz': 80, 'zkraw': 25}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
