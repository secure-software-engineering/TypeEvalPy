# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 89.96


def func2():
    return 'kaauy'


def func3():
    return {'gtpio': 40, 'qdqnn': 70, 'ercsf': 47}


def func4():
    return [48, 27, 96]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
