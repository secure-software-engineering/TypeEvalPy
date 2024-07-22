# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'jvvep'


def func2():
    return (69, 76, 16)


def func3():
    return 25.05


def func4():
    return {'zxucb': 86, 'loygt': 2, 'sqhts': 44}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
