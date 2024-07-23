# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'fmiep'


def func2():
    return {'ywbum': 76, 'hlkxe': 86, 'wfrni': 45}


def func3():
    return [20, 23, 85]


def func4():
    return (66, 68, 80)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
