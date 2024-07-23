# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 76.21


def func2():
    return {'okrpf': 56, 'bpmoc': 52, 'qbeno': 8}


def func3():
    return (11, 36, 13)


def func4():
    return [73, 12, 29]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
