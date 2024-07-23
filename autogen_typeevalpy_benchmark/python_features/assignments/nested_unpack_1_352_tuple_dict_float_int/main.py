# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (71, 53, 54)


def func2():
    return {'zcbeq': 39, 'fbwly': 1, 'ghguo': 15}


def func3():
    return 71.63


def func4():
    return 67


(a, b), (c, d) = [(func1, func2), (func3, func4)]
