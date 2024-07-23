# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 91


def func2():
    return {'jrflh': 98, 'vqzwb': 84, 'eouwv': 8}


def func3():
    return (68, 41, 47)


def func4():
    return 74.88


(a, b), (c, d) = [(func1, func2), (func3, func4)]
