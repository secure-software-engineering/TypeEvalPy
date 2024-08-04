# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'yxxkb': 97, 'ztnlk': 2, 'vscmc': 89}


def func2():
    return (94, 53, 28)


def func3():
    return [17, 46, 38]


def func4():
    return 24.67


(a, b), (c, d) = [(func1, func2), (func3, func4)]
