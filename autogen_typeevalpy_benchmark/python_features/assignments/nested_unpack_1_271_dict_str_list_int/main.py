# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'uevyz': 34, 'smwcf': 56, 'tyrkk': 76}


def func2():
    return 'zifak'


def func3():
    return [31, 42, 2]


def func4():
    return 52


(a, b), (c, d) = [(func1, func2), (func3, func4)]
