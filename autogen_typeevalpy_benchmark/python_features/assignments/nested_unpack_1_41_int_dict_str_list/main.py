# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 83


def func2():
    return {'djsdh': 25, 'agxie': 26, 'ogzra': 53}


def func3():
    return 'alsry'


def func4():
    return [44, 59, 60]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
