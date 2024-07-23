# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (72, 88, 54)


def func2():
    return 69.14


def func3():
    return 'jgicl'


def func4():
    return {'yjqqk': 20, 'pbexh': 88, 'wyaws': 13}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
