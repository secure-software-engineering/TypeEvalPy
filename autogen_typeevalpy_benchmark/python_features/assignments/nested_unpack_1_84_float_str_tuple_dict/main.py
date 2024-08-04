# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 17.03


def func2():
    return 'yfynh'


def func3():
    return (11, 33, 26)


def func4():
    return {'qodhn': 4, 'neyer': 11, 'spvov': 6}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
