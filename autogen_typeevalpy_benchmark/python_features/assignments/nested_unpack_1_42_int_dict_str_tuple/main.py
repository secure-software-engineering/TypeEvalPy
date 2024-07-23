# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 22


def func2():
    return {'dvgcc': 32, 'cxdwc': 83, 'itede': 21}


def func3():
    return 'tfkxn'


def func4():
    return (32, 74, 21)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
