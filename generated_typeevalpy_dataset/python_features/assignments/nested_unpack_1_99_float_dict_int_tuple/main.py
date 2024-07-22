# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 21.18


def func2():
    return {'tojry': 8, 'lldkg': 2, 'pmwxm': 96}


def func3():
    return 36


def func4():
    return (63, 46, 90)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
