# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 31.96


def func2():
    return [98, 21, 64]


def func3():
    return 'zmwmc'


def func4():
    return {'klgpb': 52, 'hpvrh': 47, 'acdgj': 6}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
