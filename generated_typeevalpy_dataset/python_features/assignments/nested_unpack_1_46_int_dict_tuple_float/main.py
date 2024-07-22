# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 57


def func2():
    return {'fyfdq': 53, 'dksir': 5, 'ayjam': 36}


def func3():
    return (49, 92, 76)


def func4():
    return 38.69


(a, b), (c, d) = [(func1, func2), (func3, func4)]
