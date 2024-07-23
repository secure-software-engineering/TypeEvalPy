# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'frxjz'


def func2():
    return 3


def func3():
    return {'mfsww': 22, 'tdpkt': 71, 'uyucu': 48}


def func4():
    return [54, 22, 10]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
