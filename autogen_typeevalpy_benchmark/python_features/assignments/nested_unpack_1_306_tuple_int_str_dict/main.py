# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (36, 15, 90)


def func2():
    return 19


def func3():
    return 'mwnqh'


def func4():
    return {'zodjl': 42, 'qhbwg': 63, 'yqkiq': 76}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
