# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'vxjlp': 59, 'ufcbh': 58, 'bjpjl': 63}


def func2():
    return 95.29


def func3():
    return 'uccrk'


def func4():
    return (44, 96, 86)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
