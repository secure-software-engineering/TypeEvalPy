# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'lpqsk': 17, 'lfedo': 18, 'vjkhw': 2}


def func2():
    return [10, 83, 3]


def func3():
    return 19


def func4():
    return (93, 63, 85)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
