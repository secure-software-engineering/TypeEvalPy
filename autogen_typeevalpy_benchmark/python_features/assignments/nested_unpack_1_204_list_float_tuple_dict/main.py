# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [20, 96, 55]


def func2():
    return 39.98


def func3():
    return (48, 99, 48)


def func4():
    return {'inyht': 99, 'vzonj': 3, 'nawuw': 89}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
