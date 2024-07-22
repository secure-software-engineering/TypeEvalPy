# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'dhbyi': 13, 'qgsbp': 57, 'yeyso': 1}


def func2():
    return 'hcvmo'


def func3():
    return [78, 85, 44]


def func4():
    return (27, 82, 55)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
