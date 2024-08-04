# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 38


def func2():
    return (59, 65, 78)


def func3():
    return 43.59


def func4():
    return {'ucrwo': 20, 'wlxkv': 88, 'ksiig': 61}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
