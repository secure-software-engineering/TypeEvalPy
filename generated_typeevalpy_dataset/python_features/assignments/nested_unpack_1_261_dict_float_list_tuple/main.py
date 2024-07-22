# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'ylkie': 6, 'ifzfo': 45, 'tmbet': 92}


def func2():
    return 76.39


def func3():
    return [34, 61, 75]


def func4():
    return (37, 35, 76)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
