# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'xgqkj'


def func2():
    return {'jeblg': 8, 'vodsc': 50, 'rvktf': 67}


def func3():
    return [54, 69, 88]


def func4():
    return (61, 74, 31)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
