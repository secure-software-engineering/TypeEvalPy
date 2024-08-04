# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (37, 94, 87)


def func2():
    return {'eeuaz': 28, 'glgpq': 92, 'cmwzk': 50}


def func3():
    return 91


def func4():
    return 42.91


(a, b), (c, d) = [(func1, func2), (func3, func4)]
