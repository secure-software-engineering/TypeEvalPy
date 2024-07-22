# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 75


def func2():
    return 67.94


def func3():
    return {'qqcez': 72, 'mbini': 25, 'fykxn': 2}


def func4():
    return (45, 77, 37)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
