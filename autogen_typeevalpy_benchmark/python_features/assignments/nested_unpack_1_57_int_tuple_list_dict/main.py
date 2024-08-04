# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 73


def func2():
    return (77, 11, 7)


def func3():
    return [20, 21, 97]


def func4():
    return {'qrhrm': 51, 'lhtcl': 77, 'hrmrb': 8}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
