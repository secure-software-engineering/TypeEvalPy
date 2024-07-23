# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [27, 26, 80]


def func2():
    return 25


def func3():
    return 11.88


def func4():
    return {'xkfze': 14, 'btexg': 12, 'igjvy': 95}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
