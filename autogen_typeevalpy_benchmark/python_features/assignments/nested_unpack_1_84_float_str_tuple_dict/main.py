# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 28.73


def func2():
    return 'wodwb'


def func3():
    return (48, 75, 25)


def func4():
    return {'vlvkl': 26, 'syjsl': 23, 'vhpwk': 12}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
